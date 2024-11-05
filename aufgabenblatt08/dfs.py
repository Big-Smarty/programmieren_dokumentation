def dfs(maze, x, y, end_x, end_y, path):
    # Überprüfe, ob die aktuelle Position außerhalb der Grenzen des Labyrinths liegt oder ob sie eine Wand ist, oder ob sie mit 'X' bereits markiert wurde
    # Kein gültiger Zug => kehre zurück mit FALSCH
    if (
        (x < 0)
        or (x >= len(maze[0]))
        or (y < 0)
        or (y >= len(maze))
        or (maze[y][x] == "#")
        or (maze[y][x] == "X")
    ):
        return False

    # Überprüfe, ob die aktuelle Position das Ziel ist
    # Füge die Zielposition zum Pfad hinzu
    # Das Ziel wurde erreicht => kehre zurück mit WAHR
    if (x, y) == (end_x, end_y):
        path.append((x, y))

    # Überprüfe, ob die aktuelle Zelle schon Teil des Pfades ist oder als besucht markiert wurde mit '.' oder 'X'
    # Die Zelle wurde bereits besucht => kehre zurück mit FALSCH
    if ((x, y) in path) or (maze[y][x] == ".") or (maze[y][x] == "X"):
        return False

    # Markiere die aktuelle Zelle als besucht, indem du sie mit '.' markierst
    # Füge die aktuelle Position zum Pfad hinzu
    maze[y][x] = "."
    path.append((x, y))

    # Rekursive DFS-Suche in alle vier Richtungen (unten, oben, rechts, links) // siehe 3.Rekursion und Backtracking
    # Wenn einer der Aufrufe mit WAHR zurückkehrt, wurde ein zulässiger Weg gefunden => kehre zurück mit WAHR
    directions = [(-1, -1), (0, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        return dfs(maze, x + dx, y + dy, end_x, end_y, path)

    # Entferne die aktuelle Position vom Pfad
    # Ersetzt die aktuelle Zelle mit 'X', um sie als Sackgasse zu markieren
    # Kehre zurück mit FALSCH, da kein Pfad durch diese Zelle führt
    path.remove((x, y))
    maze[y][x] = "X"
    return False
