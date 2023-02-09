from computer import*

from oo_resale_shop import*

def main():
    # First, let's make a computer
    c = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500

    )

    c2 =  Computer(
        "Mac Pro (Late 2012)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500

    )

    store = ResaleShop()
    store.buy(c)
    store.buy(c2)
    store.print_inventory(c)

    store.refurbish(c)
    store.refurbish(c2)
    store.print_inventory(c)
   
    store.update_os(c, "CHEESE BURGER")
    store.print_inventory(c)
    



# Calls the main() function when this file is run
if __name__ == "__main__": main()
