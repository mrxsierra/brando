"""
Verification & Report Generation Module for Brando.
Handles compilation of direct lookup URLs for trademarks and clash checks.
"""

import urllib.parse


def generate_validation_urls(name: str) -> dict:
    """
    Generates target lookup URLs for trademark check, search clash, and slang check.
    """
    escaped = urllib.parse.quote_plus(name)
    return {
        "uspto": f"https://tmsearch.uspto.gov/bin/showfield?f=toc&state=p1&p_search={escaped}",
        "wipo": f"https://branddb.wipo.int/branddb/en/#q={escaped}",
        "google": f"https://www.google.com/search?q=%22{escaped}%22",
        "urban_dictionary": f"https://www.urbandictionary.com/define.php?term={escaped}",
    }
