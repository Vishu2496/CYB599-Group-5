    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Math;

    operation GetBestPosition(positions : Int[], target : Int) : Int {
        let nearest = BinarySearchRec(positions, target, 0, Length(positions) - 1);
        return nearest;
    }

    function BinarySearchRec(positions : Int[], target : Int, left : Int, right : Int) : Int {
        if (left > right) {
            return left;
        }

        let mid = (left + right) / 2;
        //let mid = MidToInt(Double(left + right)) / 2.0;
        if (target == positions[(mid)]) {
            return (mid);
        }
        elif (positions[(mid)] > target  ) {
            return BinarySearchRec(positions, target, left, (mid) - 1);
        }
        else {
            return BinarySearchRec(positions, target, (mid) + 1, right);
        }
    }
 
    operation RunOrderedSearch() : Unit {
        // Define the list of positions
        let positions = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99];

        // Use the GetBestPosition operation to find the index of the best position for various targets
        Message($"The best position for 20 is: {GetBestPosition(positions, 20)}");
        Message($"The best position for 22 is: {GetBestPosition(positions, 22)}");
        Message($"The best position for 28 is: {GetBestPosition(positions, 28)}");
        Message($"The best position for 30 is: {GetBestPosition(positions, 30)}");
        Message($"The best position for 32 is: {GetBestPosition(positions, 32)}");
        Message($"The best position for 34 is: {GetBestPosition(positions, 34)}");
    }

