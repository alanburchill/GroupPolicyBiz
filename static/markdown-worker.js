function prefersMarkdown(accept) {
  const quality = new Map();
  for (const range of (accept || "").split(",")) {
    const [mediaType, ...parameters] = range.toLowerCase().split(";").map(part => part.trim());
    const weight = parameters.find(parameter => /^q\s*=/.test(parameter));
    const value = weight === undefined ? 1 : Number(weight.split("=")[1]);
    if (Number.isFinite(value) && value >= 0 && value <= 1) {
      quality.set(mediaType, Math.max(quality.get(mediaType) ?? 0, value));
    }
  }
  const markdown = quality.get("text/markdown") ?? 0;
  const html = quality.get("text/html") ?? quality.get("text/*") ?? quality.get("*/*") ?? 0;
  return markdown > 0 && markdown >= html;
}

export default {
  async fetch(request, env) {
    const wantsMarkdown = ["GET", "HEAD"].includes(request.method)
      && prefersMarkdown(request.headers.get("Accept"));
    let assetRequest = request;
    if (wantsMarkdown) {
      const headers = new Headers(request.headers);
      for (const name of ["If-None-Match", "If-Modified-Since", "Range"]) {
        headers.delete(name);
      }
      assetRequest = new Request(request, { headers });
    }
    const response = await env.ASSETS.fetch(assetRequest);
    if (response.status !== 200 || !response.headers.get("Content-Type")?.startsWith("text/html")) {
      return response;
    }

    const headers = new Headers(response.headers);
    headers.append("Vary", "Accept");
    if (wantsMarkdown) {
      const url = new URL(request.url);
      const path = url.pathname.endsWith("/") ? url.pathname + "index" : url.pathname;
      url.pathname = "/_markdown" + path + ".txt";
      url.search = "";
      const markdown = await env.ASSETS.fetch(new Request(url, { method: request.method }));
      if (markdown.ok && markdown.headers.get("Content-Type")?.startsWith("text/plain")) {
        for (const name of ["Content-Length", "Content-Encoding", "ETag", "Last-Modified", "Accept-Ranges"]) {
          headers.delete(name);
        }
        headers.set("Content-Type", "text/markdown; charset=utf-8");
        return new Response(markdown.body, { headers });
      }
    }
    return new Response(response.body, { status: response.status, headers });
  },
};
