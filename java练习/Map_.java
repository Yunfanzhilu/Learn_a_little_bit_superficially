
import jdk.swing.interop.SwingInterOpUtils;

import java.util.*;

/*
JDK8的Map接口特点
1.Map与Collection并列存在，用于保存具有映射关系的数据：Key-Value
2.Map中的key和value，可以是任何引用类型的数据，会封装到HashMap$Node对象中
3.Map中的key不允许重复
4.Map中的value可以重复
5.key null只能有1个，value null可以有多个
6.key与value一对一
 */
public class Map_ {
    public static void main(String[] args) {
        //1.Map与Collection并列存在，用于保存具有映射关系的数据：Key-Value（双列元素）
        Map map1=new HashMap();
        map1.put("a",1);
        map1.put("b",2);
        map1.put("m",6);
        map1.put("mm",7);
        map1.put("pq",9);//添加
        map1.put("qwe",2);
        map1.put("A",92);
        int aa=92;
        System.out.println("aa="+aa+1);


        //遍历map1
        Set set_map1 = map1.keySet();
        for (Object o : set_map1) {
            System.out.println("map1的keys:"+o);
        }



        int[] nums = new int[4];
        nums[0]=3;
        nums[1]=3;
        nums[2]=4;
        nums[3]=7;


        //HashMap<int,int> objectObjectHashMap = new HashMap<int,int>(); Type argument cannot be of primitive type       参数不能是原始类型
        //泛型类型参数不能是原始数据类型，而应该是对象。因为在编译时会把带泛型的转换成Object类型，而基本数据类型不属于Object，所以比如想放int类型，就需要使用它的封装类Integer类型，而不能是int
        HashMap<Integer, Integer> map2 = new HashMap<>();
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if(map2.containsKey(nums[i]))
            {
                Integer count = map2.get(nums[i]);
                count=count+1;
                map2.put(nums[i], count);

            }
            else {
                map2.put(nums[i], 1);
            }

        }
        //取出map2中key
        Set<Integer> keys = map2.keySet();
        System.out.println("map2.keys="+keys);
        Object[] objects = keys.toArray();
        System.out.println(objects[1]);

        //取出map2中value
        Object[] objects1 = map2.values().toArray();
        System.out.println(objects1[1]);
        Object o = objects1[1];


//        for(int index=0;index<nums.length;index++)
//        {
//            if(map2.get(nums[index])>(nums.length/3)&&(!ans.contains(nums[index])))
//            {
//                ans.add(nums[index]);
//            }
//        }


        System.out.println("ans="+ans);
        System.out.println(map1.get("qwe"));


    }

}

public class test01 {
    public static void main(String[] args) {
        int test01=92;
        int test02=test01*21;
        int test03=test02*17;
        int test07=test02*12;
        System.out.println(test01);
        System.out.println(test02);
        System.out.println("test07="+test07);
        System.out.println("test03="+test03);
        int test17=93;

    }

}