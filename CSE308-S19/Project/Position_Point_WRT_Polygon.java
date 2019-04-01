/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.sunyk.CSE216.preprocessing;

 
public class Position_Point_WRT_Polygon
{
 
    public static boolean onSegment(Point p, Point q, Point r)
    {
        if (q.x <= Math.max(p.x, r.x) && q.x >= Math.min(p.x, r.x)
                && q.y <= Math.max(p.y, r.y) && q.y >= Math.min(p.y, r.y))
            return true;
        return false;
    }
 
    public static double orientation(Point p, Point q, Point r)
    {
        double val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
 
        if (val == 0)
            return 0;
        return (val > 0) ? 1 : 2;
    }
 
    public static boolean doIntersect(Point p1, Point q1, Point p2, Point q2)
    {
 
        double o1 = orientation(p1, q1, p2);
        double o2 = orientation(p1, q1, q2);
        double o3 = orientation(p2, q2, p1);
        double o4 = orientation(p2, q2, q1);
 
        if (o1 != o2 && o3 != o4)
            return true;
 
        if (o1 == 0 && onSegment(p1, p2, q1))
            return true;
 
        if (o2 == 0 && onSegment(p1, q2, q1))
            return true;
 
        if (o3 == 0 && onSegment(p2, p1, q2))
            return true;
 
        if (o4 == 0 && onSegment(p2, q1, q2))
            return true;
 
        return false;
    }
 
    public static boolean isInside(Point polygon[], int n, Point p)
    {
        int INF = 10000;
        if (n < 3)
            return false;
 
        Point extreme = new Point(INF, p.y);
 
        int count = 0, i = 0;
        do
        {
            int next = (i + 1) % n;
            if (doIntersect(polygon[i], polygon[next], p, extreme))
            {
                if (orientation(polygon[i], p, polygon[next]) == 0)
                    return onSegment(polygon[i], p, polygon[next]);
 
                count++;
            }
            i = next;
        } while (i != 0);
 
        return (count & 1) == 1 ? true : false;
    }
 
    public static void main(String args[])
    {
        Point polygon1[] = { new Point(0, 0), new Point(10, 0),
                new Point(10, 10), new Point(0, 10) };
        int n = 4;
 
        Point p = new Point(20, 20);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon1: " + isInside(polygon1, n, p));
        p = new Point(5, 5);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon1: " + isInside(polygon1, n, p));
 
        Point polygon2[] = { new Point(0, 0), new Point(5, 5), new Point(5, 0) };
        n = 3;
 
        p = new Point(3, 3);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon2: " + isInside(polygon2, n, p));
        p = new Point(5, 1);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon2: " + isInside(polygon2, n, p));
        p = new Point(8, 1);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon2: " + isInside(polygon2, n, p));
 
        Point polygon3[] = { new Point(0, 0), new Point(10, 0),
                new Point(10, 10), new Point(0, 10), new Point(5, 5) };
        n = 5;
 
        p = new Point(-1, 10);
        System.out.println("Point P(" + p.x + ", " + p.y
                + ") lies inside polygon3: " + isInside(polygon3, n, p));
    }
}
