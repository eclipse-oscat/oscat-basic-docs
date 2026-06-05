import os
import glob

header = """<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

"""

repo_dir = r"G:\Geteilte Ablagen\OSCAT neu\OSCAT_DOC\oscat-basic-docs"
md_files = glob.glob(os.path.join(repo_dir, "**", "*.md"), recursive=True)

updated = 0
skipped = 0

for md_path in md_files:
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Prüfe ob Header schon da
    if "SPDX-License-Identifier: EPL-2.0" in content:
        skipped += 1
        continue
    
    # Füge Header am Anfang ein
    new_content = header + content
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    updated += 1

print(f"Updated: {updated}")
print(f"Skipped (already had header): {skipped}")
print(f"Total: {len(md_files)}")
