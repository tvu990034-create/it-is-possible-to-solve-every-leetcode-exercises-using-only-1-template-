# ================================================
# HOW TO USE:
# 1. Copy the entire content of any exercise file you want to run
# 2. Paste it right below the line that says "PASTE YOUR CODE HERE"
# 3. Save and run this file
# 
# The runner will automatically detect if it is a standalone script
# or a LeetCode-style class and run it accordingly.
# ================================================

import sys
import collections
import bisect
import re
import itertools
import string
import heapq
import math
import random
from collections import deque, defaultdict, Counter

# ====================== PASTE YOUR CODE HERE ======================
# Paste the full content of any exercise file below this line

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
               (self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])):
                return True
        return False


# ====================== AUTO EXECUTION ======================
if __name__ == "__main__":
    print("Runner started.")

    # Try to run as a full standalone script
    try:
        exec("""# PASTED CODE GOES HERE (already above)""")
        print("Standalone script executed.")
    except:
        # If it is a class Solution, use interactive mode
        try:
            sol = Solution()
            print("Detected class Solution.")

            method_name = input("Enter method name: ").strip()

            method = getattr(sol, method_name, None)
            if not method:
                print("Method not found.")
                sys.exit()

            args = []
            i = 1
            while True:
                arg = input(f"Argument {i} (press Enter to finish): ").strip()
                if not arg:
                    break
                try:
                    if arg.startswith("[") or arg.startswith("("):
                        arg = eval(arg)
                    elif arg.isdigit():
                        arg = int(arg)
                    elif "." in arg and arg.replace(".", "", 1).isdigit():
                        arg = float(arg)
                except:
                    pass
                args.append(arg)
                i += 1

            result = method(*args)
            print("Result:", result)

        except Exception as e:
            print("Error:", e)

    print("Runner finished.")