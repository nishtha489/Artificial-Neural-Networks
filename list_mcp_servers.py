#!/usr/bin/env python3
"""
Script to list available MCP (Model Context Protocol) servers.

This script provides information about MCP servers available in the
GitHub Copilot development environment.
"""

import json
import sys
import argparse

__version__ = "1.0.0"

# MCP Servers database
MCP_SERVERS = [
    {
        "id": "github",
        "name": "GitHub MCP Server",
        "category": "version-control",
        "description": "Comprehensive access to GitHub repository data and operations",
        "capabilities": [
            "Repository exploration (files, commits, branches, tags)",
            "Issue and pull request management",
            "GitHub Actions workflows and runs",
            "Code scanning and security alerts",
            "Search functionality (code, issues, PRs, users, repositories)",
            "Release management"
        ],
        "use_cases": [
            "Exploring repository structure and code",
            "Searching for specific code patterns",
            "Retrieving commit history and diffs",
            "Managing issues and pull requests",
            "Accessing GitHub Actions logs and artifacts",
            "Security vulnerability scanning"
        ]
    },
    {
        "id": "playwright",
        "name": "Playwright Browser MCP Server",
        "category": "browser-automation",
        "description": "Automated browser interaction and web testing",
        "capabilities": [
            "Navigate to URLs and interact with web pages",
            "Take screenshots and capture page snapshots",
            "Fill forms and click elements",
            "Handle dialogs and file uploads",
            "Execute JavaScript on pages",
            "Network request monitoring",
            "Console log capture"
        ],
        "use_cases": [
            "Testing web applications",
            "Capturing screenshots of UI changes",
            "Automating web interactions",
            "Verifying deployed applications",
            "Web scraping and data extraction"
        ]
    },
    {
        "id": "web-search",
        "name": "Web Search MCP Server",
        "category": "information-retrieval",
        "description": "AI-powered web search with citations",
        "capabilities": [
            "Intelligent web search with contextual answers",
            "Inline citations and source attribution",
            "Up-to-date information retrieval",
            "Factual information with verifiable sources"
        ],
        "use_cases": [
            "Researching current events or recent developments",
            "Finding up-to-date documentation",
            "Verifying information from multiple sources",
            "Discovering new technologies or trends"
        ]
    },
    {
        "id": "web-fetch",
        "name": "Web Fetch MCP Server",
        "category": "information-retrieval",
        "description": "Direct web page fetching and parsing",
        "capabilities": [
            "Fetch HTML content from URLs",
            "Convert HTML to markdown",
            "Support for pagination",
            "Raw HTML or simplified markdown output"
        ],
        "use_cases": [
            "Reading documentation pages",
            "Extracting content from websites",
            "Parsing HTML content",
            "Retrieving web resources"
        ]
    },
    {
        "id": "bash",
        "name": "Bash/Shell MCP Server",
        "category": "system",
        "description": "Command-line execution capabilities",
        "capabilities": [
            "Execute shell commands",
            "Synchronous and asynchronous execution",
            "Interactive session support",
            "Background process management",
            "Session persistence"
        ],
        "use_cases": [
            "Running build scripts",
            "Installing dependencies",
            "Running tests and linters",
            "File system operations",
            "Process management"
        ]
    },
    {
        "id": "filesystem",
        "name": "File System MCP Server",
        "category": "system",
        "description": "File and directory operations",
        "capabilities": [
            "View files and directories",
            "Create new files",
            "Edit existing files with string replacement",
            "Search files with grep and glob",
            "Handle text and binary files"
        ],
        "use_cases": [
            "Reading and writing code",
            "Searching for patterns in files",
            "File organization and management",
            "Code modifications"
        ]
    },
    {
        "id": "code-analysis",
        "name": "Code Analysis MCP Servers",
        "category": "security",
        "description": "Code quality and security analysis",
        "capabilities": [
            "GitHub Advisory Database - vulnerability checks",
            "CodeQL Checker - static code analysis",
            "Code Review - automated reviews",
            "Security scanning for dependencies",
            "CVE and security advisory lookups"
        ],
        "use_cases": [
            "Checking dependencies for vulnerabilities",
            "Static code analysis",
            "Security vulnerability detection",
            "Code quality checks",
            "Automated code reviews"
        ]
    }
]


def list_all_servers(output_format="text"):
    """
    List all available MCP servers.
    
    Args:
        output_format: Either 'text' or 'json'
    """
    if output_format == "json":
        print(json.dumps(MCP_SERVERS, indent=2))
        return
    
    print("=" * 80)
    print(f"Available MCP Servers ({len(MCP_SERVERS)} total)")
    print("=" * 80)
    print()
    
    for idx, server in enumerate(MCP_SERVERS, 1):
        print(f"{idx}. {server['name']} [{server['id']}]")
        print(f"   Category: {server['category']}")
        print(f"   Description: {server['description']}")
        print(f"   Capabilities: {len(server['capabilities'])}")
        print(f"   Use Cases: {len(server['use_cases'])}")
        print()


def list_server_details(server_id):
    """
    Show detailed information about a specific server.
    
    Args:
        server_id: ID of the server to display
    """
    server = next((s for s in MCP_SERVERS if s['id'] == server_id), None)
    
    if not server:
        print(f"Error: Server '{server_id}' not found.", file=sys.stderr)
        print(f"Available server IDs: {', '.join(s['id'] for s in MCP_SERVERS)}", file=sys.stderr)
        sys.exit(1)
    
    print("=" * 80)
    print(f"{server['name']}")
    print("=" * 80)
    print()
    print(f"ID: {server['id']}")
    print(f"Category: {server['category']}")
    print(f"Description: {server['description']}")
    print()
    
    print("Capabilities:")
    for cap in server['capabilities']:
        print(f"  • {cap}")
    print()
    
    print("Common Use Cases:")
    for use_case in server['use_cases']:
        print(f"  • {use_case}")
    print()


def list_by_category(category, output_format="text"):
    """
    List servers filtered by category.
    
    Args:
        category: Category to filter by
        output_format: Either 'text' or 'json'
    """
    filtered = [s for s in MCP_SERVERS if s['category'] == category]
    
    if not filtered:
        available = set(s['category'] for s in MCP_SERVERS)
        print(f"Error: No servers in category '{category}'.", file=sys.stderr)
        print(f"Available categories: {', '.join(sorted(available))}", file=sys.stderr)
        sys.exit(1)
    
    if output_format == "json":
        print(json.dumps(filtered, indent=2))
        return
    
    print("=" * 80)
    print(f"MCP Servers in category '{category}' ({len(filtered)} total)")
    print("=" * 80)
    print()
    
    for idx, server in enumerate(filtered, 1):
        print(f"{idx}. {server['name']} [{server['id']}]")
        print(f"   Description: {server['description']}")
        print()


def list_categories():
    """List all available categories."""
    categories = sorted(set(s['category'] for s in MCP_SERVERS))
    
    print("=" * 80)
    print(f"Available MCP Server Categories ({len(categories)} total)")
    print("=" * 80)
    print()
    
    category_counts = {}
    for server in MCP_SERVERS:
        cat = server['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    for cat in categories:
        count = category_counts[cat]
        print(f"  • {cat} ({count} server{'s' if count != 1 else ''})")
    print()


def main():
    """Main function to parse arguments and list MCP servers."""
    parser = argparse.ArgumentParser(
        description="List available MCP (Model Context Protocol) servers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # List all servers
  %(prog)s --json                   # List all servers in JSON format
  %(prog)s --server github          # Show details for GitHub server
  %(prog)s --category system        # List servers in 'system' category
  %(prog)s --categories             # List all available categories
        """
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Show program version and exit"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    parser.add_argument(
        "--server",
        metavar="ID",
        help="Show detailed information about a specific server"
    )
    
    parser.add_argument(
        "--category",
        metavar="CATEGORY",
        help="List servers in a specific category"
    )
    
    parser.add_argument(
        "--categories",
        action="store_true",
        help="List all available categories"
    )
    
    args = parser.parse_args()
    
    # Handle different modes
    if args.categories:
        list_categories()
    elif args.server:
        list_server_details(args.server)
    elif args.category:
        list_by_category(args.category, "json" if args.json else "text")
    else:
        list_all_servers("json" if args.json else "text")


if __name__ == "__main__":
    main()
