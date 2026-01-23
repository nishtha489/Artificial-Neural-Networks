#!/usr/bin/env python3
"""
MCP Servers Information Tool

This script provides quick access to information about available
Model Context Protocol (MCP) servers in the development environment.
"""

import sys
import os

# ANSI color codes for better readability
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
BOLD = '\033[1m'
END = '\033[0m'

def print_header(text):
    """Print a formatted header."""
    print(f"\n{BOLD}{BLUE}{'=' * 70}{END}")
    print(f"{BOLD}{BLUE}{text}{END}")
    print(f"{BOLD}{BLUE}{'=' * 70}{END}\n")

def list_mcp_servers():
    """List all available MCP servers with brief descriptions."""
    print_header("Available MCP Servers")
    
    servers = [
        {
            "name": "GitHub MCP Server",
            "icon": "🐙",
            "description": "Repository management, code search, CI/CD monitoring",
            "capabilities": [
                "Search code across repositories",
                "Manage issues and pull requests",
                "Monitor GitHub Actions workflows",
                "Access security scanning results"
            ]
        },
        {
            "name": "Playwright Browser MCP Server",
            "icon": "🌐",
            "description": "Browser automation and web interaction",
            "capabilities": [
                "Navigate and interact with web pages",
                "Take screenshots and page snapshots",
                "Fill forms and test UIs",
                "Monitor network requests"
            ]
        },
        {
            "name": "Bash Execution Environment",
            "icon": "💻",
            "description": "Command execution and development tasks",
            "capabilities": [
                "Execute commands (sync/async/detached)",
                "Persistent shell sessions",
                "Install packages and dependencies",
                "Run tests and build processes"
            ]
        },
        {
            "name": "File System Operations",
            "icon": "📁",
            "description": "File and directory management",
            "capabilities": [
                "Read, create, and edit files",
                "Search file contents (ripgrep)",
                "Find files by patterns (glob)",
                "Directory traversal and listing"
            ]
        },
        {
            "name": "Web Access",
            "icon": "🔍",
            "description": "Internet search and content retrieval",
            "capabilities": [
                "AI-powered web search with citations",
                "Fetch web pages as markdown",
                "Access current documentation",
                "Research APIs and libraries"
            ]
        },
        {
            "name": "Code Quality & Security",
            "icon": "🔒",
            "description": "Code review and security scanning",
            "capabilities": [
                "Automated code reviews",
                "CodeQL security analysis",
                "Dependency vulnerability checking",
                "Store codebase conventions"
            ]
        }
    ]
    
    for i, server in enumerate(servers, 1):
        print(f"{BOLD}{server['icon']}  {i}. {server['name']}{END}")
        print(f"   {CYAN}{server['description']}{END}")
        print(f"   {YELLOW}Key capabilities:{END}")
        for cap in server['capabilities']:
            print(f"      • {cap}")
        print()

def show_documentation_path():
    """Show where to find detailed documentation."""
    print_header("Documentation")
    
    doc_file = "MCP_SERVERS.md"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    doc_path = os.path.join(current_dir, doc_file)
    
    if os.path.exists(doc_path):
        print(f"📖 {BOLD}Comprehensive documentation available at:{END}")
        print(f"   {GREEN}{doc_path}{END}")
        print(f"\n💡 {YELLOW}View with:{END}")
        print(f"   cat {doc_file}")
        print(f"   less {doc_file}")
        print(f"   or open in your favorite editor")
    else:
        print(f"⚠️  Documentation file {doc_file} not found in current directory")
    print()

def show_quick_help():
    """Show quick help and usage examples."""
    print_header("Quick Usage Examples")
    
    examples = [
        ("Search for code", "Use GitHub MCP: github-mcp-server-search_code"),
        ("Run tests", "Use Bash MCP: bash command='pytest tests/'"),
        ("Edit files", "Use File System MCP: edit path='file.py' old_str='...' new_str='...'"),
        ("Browse web", "Use Browser MCP: playwright-browser_navigate url='...'"),
        ("Review code", "Use Code Quality MCP: code_review"),
        ("Web research", "Use Web Access MCP: web_search query='...'"),
    ]
    
    for task, method in examples:
        print(f"  {BOLD}{task}:{END}")
        print(f"    → {CYAN}{method}{END}\n")

def main():
    """Main function."""
    print(f"\n{BOLD}{GREEN}MCP Servers - Model Context Protocol{END}")
    print(f"{CYAN}Standardized interfaces for AI assistant interactions{END}")
    
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['--help', '-h', 'help']:
            print("\nUsage: python mcp_info.py [options]")
            print("\nOptions:")
            print("  --help, -h     Show this help message")
            print("  --list, -l     List all MCP servers")
            print("  --docs, -d     Show documentation location")
            print("  --examples, -e Show usage examples")
            print("  (no args)      Show all information")
            return
        elif arg in ['--list', '-l']:
            list_mcp_servers()
            return
        elif arg in ['--docs', '-d']:
            show_documentation_path()
            return
        elif arg in ['--examples', '-e']:
            show_quick_help()
            return
    
    # Default: show everything
    list_mcp_servers()
    show_quick_help()
    show_documentation_path()
    
    print(f"{BOLD}{GREEN}{'=' * 70}{END}")
    print(f"{BOLD}For more details, see MCP_SERVERS.md{END}")
    print(f"{BOLD}{GREEN}{'=' * 70}{END}\n")

if __name__ == "__main__":
    main()
