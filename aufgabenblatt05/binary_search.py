def binary_search(region, attempts=1):
    # 0 => kleiner, 1 => größer, 2 => richtig
    match int(
        input(
            "Ist es "
            + str((region[0] + region[1]) // 2)
            + "? (0 => kleiner, 1 => größer, 2 => richtig)\n"
        )
    ):
        case 0:
            return binary_search(
                (region[0], (region[0] + region[1]) // 2), attempts + 1
            )
        case 1:
            return binary_search(
                ((region[0] + region[1]) // 2, region[1]), attempts + 1
            )
        case 2:
            print(
                str((region[0] + region[1]) // 2)
                + " nach "
                + str(attempts)
                + " Versuch(en) gefunden\n"
            )
            return (region[0] + region[1]) // 2


binary_search((0, 1023))
