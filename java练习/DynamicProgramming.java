import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class DynamicProgramming {

    //打印字符串的子串
    public static List<String>substring(String s)
    {
        int a1=12;
        int b1=19;
    
        char[] str=s.toCharArray();
        List<String>ans=new ArrayList<>();
        int i,j;
        String tmp="";
        char[] tmp2;
        for(i=0;i<str.length;i++)
        {
            tmp=String.valueOf(str[i]);
            ans.add(tmp);
            for(j=i+1;j<str.length;j++)
            {
                tmp=tmp+String.valueOf(str[j]);
                ans.add(tmp);
            }
        }
        return ans;
    }




    //打印字符串的所有子序列（子序列比子串更自由）
//    public static List<String> subsequence(String s)
//    {
//         char[] str=s.toCharArray();
//         String path="";
//         List<String>ans=new ArrayList<>();
//         process1(str,0,ans,path);
//         return ans;
//    }
//
//public static void process1(char[]str,int index,List<String>ans,String path)
//{
//if(index==str.length)
//{
//    ans.add(path);
//    return;
//}
//String no=path;
//process1(str,index+1,ans,no);
//String yes=path+String.valueOf(str[index]);
//process1(str,index+1,ans,yes);
//}

public static List<String>subsequence(String s)
    {

        char[] str=s.toCharArray();
        String tmp="";
        int i,j;
        List<String>ans=new ArrayList<>();
        if(s==null||s.length()<=0)
        {
            return ans;
        }
        process1(str,0,ans,tmp);

         return ans;

    }

    public static void process1(char[] str,int index,List<String>ans,String tmp)
    {
        if(index==str.length)
        {

            ans.add(tmp);
            return;//这里要有返回
        }
        //要这个字符或者不要这个字符
        String yes="";
        yes=tmp+String.valueOf(str[index]);
        process1(str,index+1,ans,yes);
        String no=tmp;
        process1(str,index+1,ans,tmp);

    }


    public static List<String>subsequence_norepeat(String s)
    {

        char[] str=s.toCharArray();
        String tmp="";
        int i,j;
        HashSet<String>set=new HashSet<>();

        process_norepeat(str,0,set,tmp);
        List<String>ans=new ArrayList<>();
for(String cur:set)
{
    ans.add(cur);
}
        return ans;

    }

    public static void process_norepeat(char[] str,int index,HashSet<String>set,String tmp)
    {
        if(index==str.length)
        {

            set.add(tmp);
            return;//这里要有返回
        }
        //要这个字符或者不要这个字符
        String yes="";
        yes=tmp+String.valueOf(str[index]);
        process_norepeat(str,index+1,set,yes);
        String no=tmp;
        process_norepeat(str,index+1,set,tmp);

    }




    //打印字符串全排列
    public static ArrayList<String>permutation(String str)
    {
      ArrayList<String>res=new ArrayList<>();
      if(str==null||str.length()==0)
      {
          return res;
      }
      char[] chs=str.toCharArray();
      process_permutation(chs,0,res);

      return res;
    }
//str[0..i-1]已经做好决定的
    //str[i...]都有机会来到i位置
    //i终止位置，str当前的样子，就是一种结果，放入arraylist

    public static void process_permutation(char[] chs,int index,ArrayList<String>res)
    {
        if(index==chs.length)
        {
            res.add(String.valueOf(chs));
            return;

        }
        int i,j;
        for(i=index;i<chs.length;i++)
        {
            swap(chs,i,index);
            process_permutation(chs,index+1,res);
            swap(chs,i,index);
        }

    }
    public static void swap(char[] chs,int i,int j)
    {
        char tmp;
        tmp=chs[i];
        chs[i]=chs[j] ;
        chs[j]=tmp;
    }

    //从左往右的尝试模型1
    //1对应A  2对应B  3对应C
    //111转换为“AAA”,"KA","AK"
    public static int number(String str)
    {
      if(str==null||str.length()==0)
      {
          return 0;
      }
      char[] chs=str.toCharArray();
      int res=0;
      res=process(chs,0);
      return res;
    }
    public static int process(char[] chs,int index)
    {
        int i,j,res=0;
        if(index==chs.length)
        {
          return 1;
        }
        if(chs[index]=='0')
        {
            return 0;
        }
        if(chs[index]=='1')
        {
            res=process(chs,index+1);
            if(index+1<chs.length)
            {
                res+=process(chs,index+2);
            }
        }
        if(chs[index]=='2')
        {
            res=process(chs,index+1);
            if(index+1<chs.length&&(chs[index]>='0'&&chs[index]<='6'))
            {
                res+=process(chs,index+2);
            }
        }
        return res;


    }

    //从左往右的尝试模型2背包问题
    public static int getMaxValue(int[] w,int[] v,int bag)
    {
        int res;
        res=process(w,v,0,0,bag);
        int res2=process2(w,v,0,bag);
        return res;
    }
    //不变：w[] v[] bag
    //index...最大价值
    //0....index-1上做了货物的选择，使得你已  经达到的重量是多少alreadyW
    //如果返回-1，认为没有方案
    //如果不返回-1，认为返回的值是真实价值
    //
    public static int process(int[] w,int[] v,int index,int alreadyW,int bag)
    {
        int res=0;
        if(alreadyW>bag)
        {
            return -1;
        }
        //重量没超
        if(index==w.length)
        {
            return 0;
        }
        //如果没要这个当前货物
        int p1=process(w,v,index+1,alreadyW,bag);
        //如果要了当前货物
        int p2next=process(w,v,index+1,alreadyW+w[index],bag);
        int p2=-1;
        if(p2next!=-1)
        {
            p2=v[index]+p2next;
        }
        res=Math.max(p1,p2);
        return res;
    }
     //还剩下reset空间
    //index..货物自由选择，但是剩余空间不要小于0
    //返回index....，货物能够获得的最大价值
public static int process2(int[] w,int[]v,int index,int reset)
{
    if(reset<0)
    {
        return 0;
    }
    if(index==w.length)
    {
        return 0;
    }

    int p1=process2(w,v,index+1,reset);
    int p2=Integer.MIN_VALUE;
    if(reset>w[index]) {
        p2 = process2(w, v, index + 1, reset - w[index]);
    }
    return Math.max(p1,p2);
}


    //N皇后

    public static int NQueen(int n)
    {
        if(n<=2)
        {
            return 0;
        }
        int[] record=new int[n];
        int res=process1(0,record,n);
        return res;

    }
    //index表示第几行
    public static int process1(int index,int[] record,int n)
    {
        int res=0;
        if(index==n)
        {
            return 1;
        }
        //j表示第几列
        for(int j=0;j<n;j++)
        {
            if(isValid(record,index,j))
            {
                record[index]=j;
                res+=process1(index+1,record,n);
            }
        }



        return res;
    }

    public static boolean isValid(int[] record,int i,int j)
    {
        int k;
        for(k=0;k<i;k++)
        {
            if(j==record[k]||Math.abs(record[k]-j)==Math.abs(i-k))
            {
                return false;
            }
        }
        return true;
    }


//机器人行走
    //一共N个位置，起点是start，目标end点，需要走K步
    public static int walkWay(int N,int start,int end,int K)
    {
           int res=f(N,start,end,K);
           return res;
    }
    //一共是1~N这么多位置，固定参数
    //最终目前是E，固定参数
    //还剩rest步需要走
    //当前cur位置
    //返回方法数
    public static int f(int N,int cur,int end,int rest)
    {
        if(rest==0)
        {
            if(cur==end)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        if(cur==1)
        {
            return f(N,2,end,rest-1);
        }
        if(cur==N)
        {
            return f(N,N-1,end,rest);
        }
        return (f(N,cur+1,end,rest-1)+f(N,cur-1,end,rest-1));
    }


    //记忆化搜索优化该题
    public static int walkWay2(int N,int start,int end,int K)
    {
        int dp[][]=new int[K+1][N+1];
        int i,j;
        for(i=0;i<=K;i++)
        {
            for(j=0;j<=N;j++)
            {
                dp[i][j]=-1;
            }
        }
        int res=f2(N,start,end,K,dp);
        return res;
    }
    public static int f2(int N,int cur,int end,int rest,int[][] dp)
    {
        if(dp[rest][cur]!=-1)
        {
            return dp[rest][cur];
        }
         if(rest==0)
         {
             if(cur==end)
             {
                 dp[rest][cur]=1;
             }
             else
             {
                 dp[rest][cur]=0;
             }
             return dp[rest][cur];
         }
        if(cur==1)
        {
            dp[rest][cur]=f2(N,2,end,rest-1,dp);
            return dp[rest][cur];
        }
        else if(cur==N)
        {
            dp[rest][cur]=f2(N,N-1,end,rest,dp);
            return dp[rest][cur];
        }
        else
            {
            dp[rest][cur] = (f2(N, cur + 1, end, rest - 1,dp) + f2(N, cur - 1, end, rest - 1,dp));
        }
        return dp[rest][cur];
    }
 //动态规划
 public static int walkWay3(int N,int start,int end,int K)
 {
     int[][] dp2=new int[K+1][N+1];
     int i1,j1;
     for(i1=0;i1<=K;i1++)
     {
      dp2[0][i1]=0;
     }
     for(j1=0;j1<=N;j1++)
     {
         dp2[j1][0]=-2;
     }
     for(i1=1;i1<=K;i1++)
     {
         for(j1=1;j1<=K;j1++)
         {
             if(j1==1)
             {
                 dp2[i1][j1]=dp2[i1-1][j1+1];
             }
             if(j1==N)
             {
                 dp2[i1][j1]=dp2[i1-1][j1-1];
             }
             dp2[i1][j1]=dp2[i1-1][j1-1]+dp2[i1-1][j1+1];
         }
     }


     int res=dp2[end][start];
     return res;
 }


 //[2,7,3,5,3]一个数代表一枚硬币，aim=10，请求组成这个值最少多少硬币
public static int minCoins1(int[] arr,int aim)
     {
         int res=0;
         res=process(arr,0,aim);
         return res;
     }
     public static int process(int[] arr,int index,int rest)
     {
         if(rest<0)
         {
             return -1;
         }
         if(rest==0)
         {
             return 0;
         }
         //rest>0且有硬币
         if(index==arr.length)
         {
             return -1;
         }
         //不要这枚硬币
         int p1=process(arr,index+1,rest);
         //要这枚硬币
         int p2Next=process(arr,index+1,rest-arr[index]);
         if(p1==-1&&p2Next==-1)
         {
            return -1;
         }
         else if(p1==-1)
         {
             return (1+p2Next);

         }
        else if(p2Next==-1)
        {
            return p1;
        }
        return Math.min(p1,p2Next+1);

     }


//动态规划
    public static int minCoins3(int[] arr,int aim)
    {
        int res=0;
        int N=arr.length;
        int[][] dp=new int[N+1][aim+1];
        int row,col;
        for (row=0;row<=N;row++)
        {
             dp[row][0]=0;
        }
        for(col=1;col<=aim;col++)
        {
            dp[N][col]=-1;
        }
        for(int index=N-1;index>=0;index++)
        {
            for(int rest=1;rest<=aim;rest++)
            {
                int p1=dp[index+1][rest];
                int p2Next=-1;
                if(rest-arr[index]>=0)
                {
                    p2Next=dp[index+1][rest-arr[index]];
                }
                if(p1==-1&&p2Next==-1)
                {
                    dp[index][rest]=-1;
                }
                else
                {
                    if(p1==-1)
                    {
                        dp[index][rest]=p2Next+1;
                    }
                    if(p2Next==-1)
                    {
                        dp[index][rest]=p1;
                    }
                    dp[index][rest]=Math.min(p1,p2Next+1);
                }
            }


        }


        return dp[0][aim];
    }



    //象棋马走到x,y位置的方法数
    public static int maGetWays(int x,int y,int k)
    {
        int x1=0;
        int y1=0;
        return processma(x,y,x1,y1,k);
    }
    //从(0,0)位置出发
    //要去往(x,y)位置，必须跳step步
    //返回方法数
    public static int processma(int x,int y,int x1,int y1,int step)
    {
        if(x1<0||y1<0||x1>8||y1>9)
        {
            return 0;
        }
        if(step==0)
        {
            if(x==x1&&y==y1)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }

        int res=0;
        res=processma(x,y,x1-1,y1+2,step-1)
            +processma(x,y,x1+1,y1+2,step-1)
            +processma(x,y,x1+2,y1+1,step-1)
                +processma(x,y,x1+2,y1-1,step-1)
        +processma(x,y,x1+1,y1-2,step-1)
                +processma(x,y,x1-1,y1-2,step-1)
                +processma(x,y,x1-2,y1-1,step-1)
                +processma(x,y,x1-2,y1+1,step-1);
        return res;

    }

    //arr里都是正数，没有重复值，每一个值代表一种货币，每一种都可以使用无限张
    //最终要找零钱数是aim
    //返回找钱的方法数
public static int CoinWay1(int[] arr,int aim)
{
    return processzhang(arr,0,aim);

}
//可以自由选择arr[index....]所有的，面值
    //需要搞定的钱数是rest
    //返回找零的方法数
public static int processzhang(int[] arr,int index,int rest)
{
//    if(rest<0)
//    {
//        return -1;
//    }
//    if(rest==0)
//    {
//        return 1;
//    }
    if(index==arr.length)
    {
        if(rest==0)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    int way=0;
    for(int i=0;i*arr[index]<=rest;i++)
    {
        way+=processzhang(arr,index+1,rest-i*arr[index]);
    }
    return way;

}



//岛屿数量
    public static int numIslands(int[][] grid)
    {
        if(grid==null)
        {
            return 0;
        }
        int i,j;
        int res=0;
        int a,b;
        int chang=0 ,kuan=1;
        int area=0;
        int temp;
        for(i=0;i<grid.length;i++)
        {
            for(j=0;j<grid[0].length;j++)
            {
                if(grid[i][j]==1) {
                    res++;
                    processnumIslands(i, j, grid);
                }




            }
        }
        return res;

    }
    public static void processnumIslands(int i,int j,int[][] grid)
    {
        if(i<0||i>=grid.length||j<0||j>=grid[0].length||grid[i][j]==0||grid[i][j]==2)
        {
            return ;
        }



        grid[i][j] = 2;



        processnumIslands(i+1,j,grid);
        processnumIslands(i-1,j,grid);

        processnumIslands(i,j+1,grid);
        processnumIslands(i,j-1,grid);





    }


    //岛屿最大面积
    public static int numIslandsMaxArea(int[][] grid)
    {
        if(grid==null)
        {
            return 0;
        }
        int i,j;
        int res=0;
        int a,b;
        int chang=0 ,kuan=1;
        int area=0;
        int temp=0;
        for(i=0;i<grid.length;i++)
        {
            for(j=0;j<grid[0].length;j++)
            {
                if(grid[i][j]==1) {
                    res++;
                    area=processnumIslandsMaxArea(i, j, grid);
                    temp=area;
                }

             area=Math.max(temp,area);


            }
        }
        return area;

    }
    public static int processnumIslandsMaxArea(int i,int j,int[][] grid)
    {

        int area;
        if(i<0||i>=grid.length||j<0||j>=grid[0].length||grid[i][j]==2||grid[i][j]==0)
        {

            return 0;
        }

        grid[i][j] = 2;

            area = 1;


        area+=processnumIslandsMaxArea(i+1,j,grid);
        area+=processnumIslandsMaxArea(i-1,j,grid);
        area+=processnumIslandsMaxArea(i,j+1,grid);
        area+=processnumIslandsMaxArea(i,j-1,grid);


        return area;





    }
    //范围上尝试的模型
//数组arr,代表述职不同的智跑排成一条线
    //A和B一次只能拿最左或者最右的牌
    //返回获胜者的分数,A和B都取对自己最有利的方式拿牌
//    public static int win1(int[] arr)
//    {
//        if(arr==null||arr.length==0)
//        {
//            return 0;
//        }
//        int ans;
//        ans=Math.max(f(arr,0,arr.length-1),s(arr,0,arr.length-1));
//        return ans;
//    }
//    public static int f(int[] arr,int L,int R)
//    {
//        int ans=0;
//        if(L==R)//base case
//        {
//            ans=arr[L];
//            return ans;
//        }
//        int p1=arr[L]+s(arr,L+1,R);
//        int p2=arr[R]+s(arr,L,R-1);
//        ans=Math.max(p1,p2);
//        return ans;
//    }
//
//    public static int s(int[] arr,int L,int R)
//    {
//        int ans=0;
//        if(L==R)
//        {
//            ans=0;
//            return ans;
//        }
//        int p1=f(arr,L+1,R)+arr[L];
//        int p2=f(arr,L,R-1)+arr[R];
//    }






    public static void main(String[] args)
    {
         System.out.print("该字符的所有子序列：");
         String a1="abcabcqk";
         String a2="qaxz";
         List<String>ans1=subsequence(a1);
         System.out.print(ans1);
         System.out.println("");

         System.out.print("该字符的所有子序列（不包含重复子序列）：");
         List<String>ans3=subsequence_norepeat(a1);
         System.out.print(ans3);
         System.out.println("");


         System.out.print("该字符的所有子串：");
         List<String>ans2=substring(a1);
         System.out.print(ans2);
         System.out.println("");

        System.out.print("该字符的全排列：");
        ArrayList<String>ans4= permutation(a1);
        System.out.print(ans4);
        System.out.println("");

        System.out.print("转换的总数：");
        String a7="111111";
        int ans5= number(a7);
        System.out.print(ans5);
        System.out.println("");

        System.out.print("所能获得的最大价值为：");
       int[] w={2,3,1,9};
       int[] v={2,3,1,9};
       int bag=10;
       int ans6=getMaxValue(w,v,bag);
       System.out.print(ans6);
       System.out.println("");


        System.out.print("N皇后：");
        int num=8;
        int ans7=NQueen(num);
        System.out.print(ans7);
        System.out.println("");

        System.out.print("机器人行走方法1：");
        int ans8,ans9,ans10;
        ans8=walkWay(5,2,4,4);
        ans9=walkWay2(5,2,4,4);
      //  ans10=walkWay3(5,2,4,3);
        System.out.println(ans8);
        System.out.print("机器人行走方法2：");
        System.out.println(ans9);
       // System.out.println(ans10);


        System.out.print("组硬币(递归)：");
        int[] arr={2,3,100,7,1,6,7,87};
        int ans11=minCoins1(arr,12);
        System.out.print(ans11);
        System.out.println("");

        System.out.print("组硬币(动态规划)：");
        int[] arr2={2,3,100,7,1,6,7,12};
        int ans12=minCoins1(arr2,12);
        System.out.print(ans12);
        System.out.println("");

        System.out.print("马走的方法数：");
        int x=7;
        int y=7;
        int step=10;
        int ans13=processma(x,y,0,0,step);
        System.out.print(ans13);
        System.out.println("");


        System.out.print("找钱方法数：");
        int[] arrzhang={5,10,25,1};
        int aim=15;
        int ans14=processzhang(arrzhang,0,15);
        System.out.print(ans14);
        System.out.println("");

        System.out.print("岛屿数量：");


        int[][] grid1={{1,1,1,1,0},
                {1,1,0,1,0},
                {1,1,0,0,0},
                {0,0,0,0,0},
        };
        int ans15=numIslands(grid1);
        System.out.print(ans15);
        System.out.println("");

        int[][] grid2={{1,1,1,1,0},
                       {1,1,0,1,0},
                       {1,1,0,0,0},
                      {0,0,0,0,0},};
        System.out.print("岛屿最大面积：");
        int ans16=numIslandsMaxArea(grid2);
        System.out.print(ans16);
        System.out.println("");



    }
}
