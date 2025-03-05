from pathlib import Path

base = Path.home()
print(base)

guide = Path(base, "Europe", "Spain", Path("Bacelona", "Sagrada_Familia.txt"))
print(guide)

guide2 = guide.with_name("La_Pedrera.txt")
print(guide2)

print(guide.parent.parent.parent)

# guide = Path(Path.home(), "Documents")
# for txt in Path(guide).glob("**/*.txt"):
#     print(txt)

guide = Path("Europe", "Spain", "Barcelona", "Madrid", "Sagrada_Familia.txt")
in_europe = guide.relative_to(Path("Europe"))
print(in_europe)
in_spain = guide.relative_to(Path("Europe", "Spain"))
print(in_spain)

