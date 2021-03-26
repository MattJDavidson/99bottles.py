class Bottles(object):
    def verse(self, number):
        if number==2:
            return ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                    "Take one down and pass it around, 1 bottle of beer on the wall.")
        if number==1:
            return ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                    "Take it down and pass it around, no more bottles of beer on the wall.")
        if number ==0:
            return ("No more bottles of beer on the wall, no more bottles of beer.\n"
                    "Go to the store and buy some more, 99 bottles of beer on the wall.")
        return (f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
                    f"Take one down and pass it around, {number-1} bottles of beer on the wall.")

    def verses(self, start, end):
        output =""
        while start>=end:
            output+=self.verse(start) + "\n\n"
            start -=1
        return output[:-2]

    def song(self):
        return self.verses(99,0)


def main():
    Bottles()


if __name__ == '__main__':
    main()

