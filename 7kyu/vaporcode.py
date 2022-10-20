"""
7kyu "V A P O R C O D E" kata
https://www.codewars.com/kata/5966eeb31b229e44eb00007a
Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.
Note that spaces should be ignored in this case.
20/10/22
"""
import codewars_test as test


def vaporcode(s: str) -> str:
    return "  ".join([x.upper() for x in s if x != " "])


@test.describe("Basic Tests")
def __():
    @test.it("Some Examples")
    def __():
        test.assert_equals(vaporcode("Lets go to the movies"),
                           "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
        test.assert_equals(vaporcode("Why isn't my code working?"),
                           "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")
