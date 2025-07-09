import asyncio

from fastmcp import Client


async def main():
    # Connect via SSE
    async with Client("http://localhost:8000/sse") as client:
        print("=== Tool Test ===")

        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(result.structured_content)
        print(f"Result: {result.data}")

        print("=== Resource Test ===")

        templates = await client.list_resource_templates()

        for template in templates:
            print(f"Template URI: {template.uriTemplate}")
            print(f"Name: {template.name}")
            print(f"Description: {template.description}")

        result = await client.read_resource("users://1/profile")
        print(result)

        print("=== Prompt Test ===")
        prompts = await client.list_prompts()
        # prompts -> list[mcp.types.Prompt]

        for prompt in prompts:
            print(f"Prompt: {prompt.name}")
            print(f"Description: {prompt.description}")
            if prompt.arguments:
                print(f"Arguments: {[arg.name for arg in prompt.arguments]}")

        # Prompt with simple arguments
        result = await client.get_prompt(
            "summarize_request", {"text": "This is a sample text for summarization."}
        )

        # Access the personalized messages
        for message in result.messages:
            print(f"Generated message: {message.content}")


if __name__ == "__main__":
    asyncio.run(main())
