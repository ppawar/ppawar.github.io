package edu.sunyk.CSE216.preprocessing;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author SUNY Korea CS
 */
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

public class JsonSimpleReadExample {

    public static void main(String[] args) {

        JSONParser parser = new JSONParser();

        try {

            Object obj = parser.parse(new FileReader("resources\\coordinates.json"));

            JSONObject jsonObject = (JSONObject) obj;
            System.out.println(jsonObject);

            String type = (String) jsonObject.get("type");
            System.out.println(type);

            // loop array
            JSONArray coord = (JSONArray) jsonObject.get("coordinates");
            System.out.println(coord.get(0));
            JSONArray coordList = (JSONArray) coord.get(0);
            Iterator iterator = coordList.iterator();
            ArrayList<Point> allPoints = new ArrayList();
            while (iterator.hasNext()) {
                JSONArray oneCoord = (JSONArray) iterator.next();
                Point p1 = new Point((double) oneCoord.get(0), (double) oneCoord.get(1));  
                System.out.println(p1.x + " " + p1.y);
                allPoints.add(p1);
            }
            Point[] pointsArray = new Point[allPoints.size()];
            allPoints.toArray(pointsArray);
            Point checkPoint = new Point(13.4041093176, -14.9667637739);
            boolean status = Position_Point_WRT_Polygon.isInside(pointsArray, pointsArray.length, checkPoint);
            System.out.println("Status = " + status);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

    }

}