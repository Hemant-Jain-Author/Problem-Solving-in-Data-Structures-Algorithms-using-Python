int TopDownFunction(int dp[], int ways[], int target ) {
    // Base Case
    if(target == 0)
        return 0;

    if (dp[target] != INVALID) {
        return dp[target];
    }

    // Recursion
    for (int i = 0; i < ways.length; i++) {
        dp[target] = min(dp[target], TopDownFunction(dp, ways, target - ways[i]) + cost);
    }
    return dp[target];
}

int TopDownFunction(int ways[], int target ) {
    int dp[target];
    fill dp[] with value INVALID;
    return TopDownFunction(dp, ways, target);
}

int BottomUpFunction( int ways[], int target ) { 
    int dp[target];
    fill dp[] array with value INVALID;
    dp[0] = 0; // Base value.

    for (int i = 1; i <= target; i++) {
        for (int j = 0; j < ways.length; j++) {
            // For all fusible ways.
            dp[i] = min(dp[i], dp[i - ways[j]] + cost);  
        }
    }
    
    return dp[target]; 
}


int TopDownFunction(int dp[], int ways[], int target ) {
    // Base Case
    if(target == 0)
        return 0;

    if (dp[target] != 0) {
        return dp[target];
    }

    // Recursion
    for (int i = 0; i < ways.length && ways[i] <= i; i++) {
        // For all fusible ways.
        dp[target] += TopDownFunction(dp, ways, target - ways[i]);
    }
    return dp[target];
}

int TopDownFunction(int ways[], int target ) {
    int dp[target];
    return TopDownFunction(dp, ways, target);
}


int BottomUpFunction( int ways[], int target ) { 
    int dp[target];

    for (int i = 1; i <= target; i++) {
        for (int j = 0; j < ways.length && ways[i] <= i ; j++) {
            // For all fusible ways.
            dp[i] += dp[i - ways[j]];  
        }
    } 
    return dp[target]; 
}

int TopDownFunction(int costs[]) {
    int n = costs.length;
    int dp[n][n];
    for (int[] row : dp)
        fill row[] array with value INVALID;

    return TopDownFunction(dp, costs, 0, n-1);
}

int TopDownFunction(int dp[][], int costs[], int i, int j ) {
    // Base Case
    if(i == j)
        return 0;

    if (dp[i][j] != INVALID) {
        return dp[i][j];
    }

    // Recursion
    for (int k = i; k < j; k++) {
        dp[i][j] = Min (dp[i][j], TopDownFunction(dp, costs, i, k) + costs[k] +                             TopDownFunction(dp, costs, k+1, j));
    }
    return dp[i][j];
}

int BottomUpFunction(int costs[]) { 
    int n = costs.length;
    int dp[n][n];
    for (int row : dp)
        fill array row[] with value INVALID;

    for(int l = 1; l<n; l++) { // l is length of range.
        for(int i = 1, j = i+l; j<n; i++,j++) {
            for(int k = i; k<j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + costs[k] + dp[k+1][j]);
            }
        }
     }

     return dp[1][n-1];
}


for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        // incremental found pattern of sub-problem.
    }
}

for (int l = 1; l < n; l++) {  // Range.
    for (int i = 0, j = i+l; j < n; i++, j++) {
        // incremental calculation of sub-problem 
        // with increasing range.
    }
}

for (int i = 1; i <= m; i++) { // First string index.
    for (int j = 1; j <= n; j++) { // Second string index.
            // Comparison of two strings.    
    }
}


int BottomUpFunction(int costs[]) {
    int n = costs.length;
    int dp[n][2];

    /* Initialization of 0th state of various types.*/
    dp[0][1] = /* Initialization value */
    dp[0][0] = /* Initialization value */ 

    for (int i = 1; i < n; ++i) {
        dp[i][1] = /*Max values based on previous states.*/
        dp[i][0] = /*Max values based on previous states.*/
    }
    return Math.max(dp[n-1][1] , dp[n-1][0]);
}