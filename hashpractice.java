import java.util.HashMap;

public class hashpractice {

    //哈希函数（例如MD5）的特性，1输入域无限，输出域有限
    //2相同的输入，相同的输出，哈希函数不存在随机性
    //3不同的输入也有可能相同的输出（哈希碰撞）
    //4哈希函数输出均匀性，离散性



    //设计RandomPool结构，包含三个功能(要求时间复杂度O(1))：1、insert(key):将某个key加入到该结构中，做到不重复加入
    //2、delte(key)：将原本结构中的某个key移除
    //3、getRandom():等概率返回结构中的任何一个key
    public static class Pool<K>
    {
        private HashMap<K,Integer>keyIndexMap;
        private HashMap<Integer,K>IndexkeyMap;
        private int size;

        public Pool()
        {
            this.keyIndexMap=new HashMap<K,Integer>();
            this.IndexkeyMap=new HashMap<Integer,K>();
            this.size=0;
        }

        public void insert(K key)
        {
            if(!this.keyIndexMap.containsKey(key))
            {
                this.keyIndexMap.put(key,this.size);
                this.IndexkeyMap.put(this.size++,key);

            }
        }
        public void delete(K key)
        {
            if(this.keyIndexMap.containsKey(key))
            {
                int deleteIndex=this.keyIndexMap.get(key);
                int lastindex=--this.size;
                K lastkey=this.IndexkeyMap.get(lastindex);
                this.keyIndexMap.put(lastkey,deleteIndex);
                this.keyIndexMap.remove(key);
                this.IndexkeyMap.put(deleteIndex,lastkey);
                this.IndexkeyMap.remove(lastkey);

            }
        }

        public K getRandom()
        {
            if(this.size==0)
            {
                return null;
            }
            int randomIndex=(int)(Math.random()*this.size);//0~size-1
            return this.IndexkeyMap.get(randomIndex);
        }
    }
    public static void main(String[] args)
    {
      Pool<String>pool=new Pool<String>();
      pool.insert("jiang1");
        pool.insert("jiang2");
        pool.insert("jiang3");
        System.out.println(pool.getRandom());


        //简单讲下位图
        int[] arr=new int[10];//320bit
        //arr[0] int 0~31
        //arr[1] int 32~63
        //arr[2] int 64~95

        int i=169;//想去的第169个bit的状态
        int numindex=178/32;
        int bitindex=178%32;

        //拿到169位的状态
        int s=((arr[numindex]>>(bitindex))&1);

        //把169位状态改成1
        arr[numindex]=arr[numindex]|(1<<(bitindex));

        //把169位状态成0
        arr[numindex]=arr[numindex]&(~(1<<bitindex));
    }
}
