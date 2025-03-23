package com.rsk;

public class Program {
    public static void main(String[] args) {
        Meeting m = new com.rsk.Meeting();

//        m.title = "Emergency";
        System.out.println(m.title);

        com.rsk.Meeting.build();

        com.rsk.Utils.saveMeeting(m);
    }
}
