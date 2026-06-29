from duckduckgo_search import DDGS


def web_search(query):
    """
    Search the web using DuckDuckGo.
    Returns the top 5 search results.
    """

    try:
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for result in search_results:
                results.append(
                    f"Title: {result['title']}\n"
                    f"Link: {result['href']}\n"
                    f"Summary: {result['body']}\n"
                )

        return "\n\n".join(results)

    except Exception as e:
        return f"Web search failed: {e}"


def calculator(expression):
    """
    Simple calculator tool.
    """

    try:
        answer = eval(expression)
        return f"The answer is {answer}"

    except Exception:
        return "Invalid mathematical expression."