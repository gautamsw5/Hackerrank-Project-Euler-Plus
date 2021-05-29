function processData(input)
{
    var N = 60001, mod = 1000000007, t, x;
    var arr = input.split("\n");
    var dp = [1];
    for(var i = 1; i < N; i++)
        dp.push(0);
    for(var i=1; i<N; i++)
        for(var j=i; j<N; j++)
        dp[j] = (dp[j] + dp[j-i])%mod;
    var t = parseInt(arr[0]);
    for(var i = 1; i <= t; i++)
        console.log(dp[parseInt(arr[i])]);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
