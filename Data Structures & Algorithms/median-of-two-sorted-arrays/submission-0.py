class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # you want to find the left partition of the "merged array" without merging the array
        # get the smaller array and run binary search
        # you search for the middle value and then check the bigger array if the left partition is correct
        # if not, you run binary search again and switch the pointers


        # initalize our arrays and totals
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        # set up variabls for binary search
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            # initalize all the end variables for checking if the left partition is correct
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float ("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float ("infinity")

            # check if left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)

                # max value of the left partition and the min value of the right partition
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        
            elif Aleft > Bright:
                r = i - 1

            else:
                l = i + 1