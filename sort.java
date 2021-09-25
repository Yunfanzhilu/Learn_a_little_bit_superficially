import java.util.Arrays;

public class sort {
//选择排序
    public static void SelectSort(int[] arr) {
        if (arr == null || arr.length < 2) {
            return;
        }
        int i, j, mininumidex;
        //从前往后
        for (i = 0; i < arr.length; i++)
        {
            mininumidex = i;
            for (j = i + 1; j < arr.length; j++)
            {
                if (arr[j] < arr[mininumidex])
                {
                    mininumidex=j;
                }
            }
            swap(arr,i,mininumidex);
        }
    }


    //冒泡排序
    public static void BubbleSort1(int[] arr)
    {
        if(arr==null || arr.length<2)
        {
            return;
        }
        int i,j;
        for(i=arr.length-1;i>=0;i--)
        {
            for(j=0;j<i;j++)
            {
                if(arr[j]>arr[j+1])
                {
                    swap(arr,j,j+1);
                }
            }

        }
    }
    //插入排序
    public static void InsertSort(int[] arr)
    {
        if(arr==null||arr.length<2)
        {
            return;
        }
        int i,j;
        for(i=1;i<arr.length;i++)
        {
            for(j=i-1;j>=0&&arr[j+1]<arr[j];j--)
            {
                swap(arr,j,j+1);
            }
        }




    }





    //归并排序（递归）（要求一个数左边干什么或者一个数右边满足什么要求，想一想归并排序，例如求小和）
    //整体是递归的，左边排好序+右边排好序+merge让整体有序  O(N*logN)
    public static void MergeSort(int[] arr)
    {
        if(arr==null||arr.length==0)
        {
            return ;
        }
        process(arr,0,arr.length-1);
    }
    public static void process(int[] arr,int L,int R)
    {
        if(L==R)
        {
            return;
        }
        //int mid=L+((R-L)>>1);
        int mid=(L+R)/2;
        process(arr,L,mid);
        process(arr,mid+1,R);
        merge(arr,L,mid,R);
    }
    public static void merge(int[] arr,int L,int mid,int R)
    {
        int[] help=new int[R-L+1];
        int i=0,j=0;
        int p1=L;//左边块起点
        int p2=mid+1;//右边块起点

        while(p1<=mid&&p2<=R)
        {
            if(arr[p1]<arr[p2])
            {
                help[i]=arr[p1];
                i++;
                p1++;
            }
            else
            {
                help[i]=arr[p2];
                i++;
                p2++;
            }
        }

        while(p1<=mid)
        {
            help[i]=arr[p1];
            i++;
            p1++;
        }
        while (p2<=R)
        {
            help[i]=arr[p2];
            i++;
            p2++;
        }
        for(j=0;j<help.length;j++)
        {
            arr[L+j]=help[j];
        }
    }


    //归并排序（非递归）
    public static void MergeSort_Nonrecursive(int[] arr)
    {
        if (arr==null||arr.length<2)
        {
            return;
        }
        int N=arr.length;
        int MergeSize=1;//当前有序地左组长度
        while(MergeSize<N)
        {
            int L=0;
            while(L<N)
            {
                int M=L+MergeSize-1;
                if(M>=N)
                {break;}
                int R=Math.min(M+MergeSize,N-1);
                merge(arr,L,M,R);
                L=R+1;
            }
        MergeSize=(MergeSize)*2;
        }
    }

//快速排序
    public static void QuickSort(int[] arr)
    {
        if(arr.length<2||arr==null)
        {
            return;
        }
        QuickSortProcess3point0(arr,0,arr.length-1);
    }
public static void QuickSortProcess3point0(int[] arr,int L,int R)
{
    if(L<R)
    {
        swap(arr,L+(int)(Math.random()*(R-L+1)),R);
        int[] p=partition(arr,L,R);
        QuickSortProcess3point0 (arr,L,p[0]-1);
        QuickSortProcess3point0(arr,p[1]+1,R);
    }
}
      //这是一个处理arr[L---R]的函数
     //默认以arr[R]做划分，<R    ==R     >R  荷兰国旗问题
    //快排3.0版本 刚好打点到中间时时间复杂度T(N)=T(N/2)+T(N/2)+O(N),空间时间复杂度O(logN)
    //返回等于区域（左边界，右边界），返回一个长度为2的数组
    public static int[] partition(int[] arr,int L,int R)
    {

      int less=L-1;//左边界
      int more=R;//右边界
      while(L<more)
      {
          if(arr[L]<arr[R])//[i]<num，当前数和<=区下一个数交换，<=区++,i++
          {
              swap(arr,L,less+1);
              L++;
              less++;
          }
          else if(arr[L]==arr[R])//[i]=num,i++
              {
              L++;

          }
          else//[i]>num,[i]与>区前一个交换，>区左扩，i不变
          {
              swap(arr,L,more-1);
              more--;
          }
      }

      swap(arr,more,R);
      int[] p=new int[2];
      p[0]=less+1;
      p[1]=more;
        return p;
    }

    //堆排序（用数组实现的完全二叉树）==优先级队列,heapinsert从小往上PK，heapify从上往下PK
    public static void HeapSort(int[] arr)
    {
        if(arr==null ||arr.length<2)
        {
            return;
        }
        //建立堆
        int i,j;
        for(i=0;i<arr.length;i++)//O(N)
        {
            heapInsert(arr,i);//O(logN)
        }
        int heapsize=arr.length;
        swap(arr,0,--heapsize);//(开头位置与堆的最后一个位置交换)
while(heapsize>0)
{
    heapify(arr,0,heapsize);//O(logN)
    swap(arr,0,--heapsize);
}

    }
    public static void heapInsert(int[] arr,int index)
    {
        if(arr==null)
        {
            return;
        }
        while(arr[index]>arr[(index-1)/2])
        {
            swap(arr,index,((index-1)/2));
            index=(index-1)/2;
        }
    }


    //heapify，堆上最后一个数字换成堆顶，堆顶选left或right选一个PK
    //某个数在index位置，能否往下移动
    public static  void heapify(int[] arr,int index,int heapsize)
    {
        int left=index*2+1;//左孩子的下标
            while(left<heapsize)
            {//两个孩子中，谁的值更大，谁把下标给largest
                int largest;
                if((left+1<heapsize)&&arr[left]<arr[left+1])
                {
                    largest=left+1;
                }
                else
                    {
                  largest=left;
            }
                //父与孩子之间，谁的值更大，谁把下标给largest
                if(arr[index]<arr[largest])
                {
                    largest=index;
                }
                if(largest==index)
                {
                    break;
                }
                swap(arr,largest,index);
                left=index*2+1;



            }
    }



        public static void swap ( int[] arr, int i, int j)
        {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }








        //桶排序(用队列实现，先进桶的先出来)
public static void RadixSort(int[] arr)
{
    if(arr==null||arr.length<2)
    {
        return;
    }
    int temp=maxbits(arr);
    RadixSortPorcess(arr,0,arr.length-1,temp);
}
public static int maxbits(int[] arr)//找到一组数中最大的数有多少位
{
    int max=Integer.MIN_VALUE;
    for(int i=0;i<arr.length;i++)
    {
        max=Math.max(max,arr[i]);

    }
    int res=0;
    while(max!=0)
    {
        res++;
        max=max/10;
    }
    return res;
}
public static void RadixSortPorcess(int[] arr,int L,int R,int digit)
    {
        int radix=10;
        int i=0,j=0;
        //有多少数准备多少辅助空间
        int[] bucket=new int [R-L+1];
        for(int d=1;d<=digit;d++)//有多少位就进出几次
        {
            //10个空间
            //count[0]当前位（d位）是0的数字有多少个
            //count[1]当前位（d位）是(0和1)的数字有多少个
            //count[2]当前位（d位）是(0,1和2)的数字有多少个
            // count[i]当前位（d位）是(0...i)的数字有多少个
            int[] count=new int[radix];
            for(i=L;i<=R;i++)
            {
                j=getDigit(arr[i],d);
                count[j]++;
            }
            for(i=R;i>=L;i--)
            {
                j=getDigit(arr[i],d);
                bucket[count[j]-1]=arr[i];
                count[j]--;
            }
            for(i=L,j=0;j<=R;i++,j++)
            {
                arr[i]=bucket[j];
            }

        }
    }

public static int getDigit(int x,int d)
{
    return ((x/((int)Math.pow(10,d-1)))%10);
}
















//对数器
    //使用java自带的函数对比
    public static void comparator(int[] arr)
    {
        Arrays.sort(arr);
    }
    //2、实现一个随机样本产生器
    public static int[] generateRandomArray(int maxSize, int maxValue)
    {
        //产生随机数范围为[0,maxSize]
        int[] arr = new int[(int) ((maxSize + 1) * Math.random())];
        for (int i = 0; i < arr.length; i++) {
            //产生[-maxValue,maxValue]的元素
            arr[i] = (int) ((maxValue + 1) * Math.random()) - (int) (maxValue * Math.random());
        }
        return arr;
    }

    //拷贝数组
    public static int[] copyArray(int[] arr)
    {
        if (arr == null) {
            return null;
        }
        int[] res = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            res[i] = arr[i];
        }
        return res;
    }

    //3、实现比对的方法
    public static boolean isEqual(int[] arr1, int[] arr2)
    {
        if ((arr1 == null && arr2 != null) || (arr1 != null && arr2 == null)) {
            return false;
        }
        if (arr1 == null && arr2 == null) {
            return true;
        }
        if (arr1.length != arr2.length) {
            return false;
        }
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }

    //5、如果有一个样本使得比对出错，打印样本分析是哪个方法出错
    public static void printArray(int[] arr) {
        if (arr == null) {
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }











    public static void main(String[] args)
    {
//        int[] arr={6,1,8,1,22,43,1,78,9,2,167,111,78,6};
//        SelectSort(arr);
//        System.out.print("选择排序：");
//        for(int i=0;i<arr.length;i++)
//        {
//            System.out.print(arr[i]);
//            System.out.print(",");
//        }
//        int testTime = 50000;
//        int maxSize = 100;
//        int maxValue = 100;
//        boolean succeed = true;
//        //4、把方法a和方法b比对很多次来验证方法a是否正确
//        for (int i = 0; i < testTime; i++) {
//            int[] arr1 = generateRandomArray(maxSize, maxValue);
//            int[] arr2 = copyArray(arr1);
//            BubbleSort1(arr1);
//            comparator(arr2);
//            if (!isEqual(arr1, arr2)) {
//                succeed = false;
//                break;
//            }
//        }
//        System.out.println(succeed ? "您的代码完全正确" : "还存在问题，请查找");
        int maxSize = 100;
        int maxValue = 100;
        int[] arr = generateRandomArray(maxSize, maxValue);
        System.out.println("选择排序：");
        printArray(arr);
        SelectSort(arr);
        printArray(arr);



        System.out.println("冒泡排序：");
        int[] arr2 = generateRandomArray(maxSize, maxValue);
        printArray(arr2);
        BubbleSort1(arr2);
        printArray(arr2);



        System.out.println("插入排序：");
        int[] arr3 = generateRandomArray(maxSize, maxValue);
        printArray(arr3);
        InsertSort(arr3);
        printArray(arr3);

        System.out.println("归并排序：");
        //int[] arr4 = generateRandomArray(maxSize, maxValue);
        int[] arr4={-7,-18,-1,88,1,91,769,23,0,3,79};
        MergeSort(arr4);
        printArray(arr4);

        System.out.println("归并排序(非递归)：");
        //int[] arr4 = generateRandomArray(maxSize, maxValue);
        int[] arr5={-7,-18,-1,88,1,91,769,23,0,3,79,12};
        MergeSort(arr5);
        printArray(arr5);

        System.out.println("快速排序3.0：");
        //int[] arr4 = generateRandomArray(maxSize, maxValue);
        int[] arr6={-7,-18,-1,88,1,91,769,23,0,3,79,12};
        QuickSort(arr6);
        printArray(arr6);


        System.out.println("堆排序：");
        //int[] arr4 = generateRandomArray(maxSize, maxValue);
        int[] arr7={-7,-18,-1,88,1,91,769,23,0,3,79,12,87};
        int[] arr8={1,2};
        QuickSort(arr7);
        printArray(arr7);

    }



}
