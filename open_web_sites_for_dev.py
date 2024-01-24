# Purpose: Open web sites for VectorScript development.
# Author: Katsutoshi Machida
# Created: 2024-01-24
# Last update: 2024-01-24
# License: MIT License
# Version: 1.0.0
# Usage: Run this script in Vectorworks.
# Limitation: Vectorworks 2023 or later.
# Python: 3.9.2
# note: Some URLs in this script include developer websites for Japanese.

import vs


urls = [
    'https://www.aanda.co.jp/develop/ScriptReference/ScriptFunctionReference.html',
    'https://www.aanda.co.jp/develop/ScriptReference/Appendix/Appendix.html',
    'https://developer.vectorworks.net/index.php?title=VS:Function_Reference',
    'https://developer.vectorworks.net/index.php/VS:Function_Reference_Appendix'
    ]

for url in urls:
    vs.OpenURL(url)