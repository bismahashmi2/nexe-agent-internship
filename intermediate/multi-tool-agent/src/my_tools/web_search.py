from ddgs import DDGS
from agents import function_tool


@function_tool
def web_search(query: str) -> dict:
    """
    Searches the web and returns top trusted results
    """

    try:

        results = []

        blocked_domains = [
            "quora.com",
            "pinterest.com"
        ]

        trusted_domains = [
            "ieee.org",
            "techcrunch.com",
            "openai.com",
            "huggingface.co",
            "theverge.com",
            "wired.com",
            "arxiv.org"
        ]

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=8
            )

            for r in search_results:

                if not r:
                    continue

                title = r.get("title", "")
                link = r.get("href", "")
                snippet = r.get("body", "")

                # Skip blocked domains
                if any(domain in link for domain in blocked_domains):
                    continue

                results.append({
                    "title": title,
                    "link": link,
                    "snippet": snippet,
                    "trusted_source": any(
                        domain in link
                        for domain in trusted_domains
                    )
                })

                if len(results) >= 3:
                    break

        print("Web search tool fired ---->")

        return {
            "tool_used": "web_search",
            "response": {
                "query": query,
                "total_results": len(results),
                "results": results
            }
        }

    except Exception as e:

        return {
            "tool_used": "web_search",
            "error": str(e)
        }