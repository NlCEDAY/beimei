package com.wyw.ingestion.data.mongo;

import com.wyw.ingestion.common.Tuple;
import com.mongodb.BasicDBObject;

//mongo parser
public class UserFriendsParser extends com.wyw.ingestion.data.UserFriendsParser<Tuple<BasicDBObject, BasicDBObject>> {
    //parse the record
    @Override
    public Tuple<BasicDBObject, BasicDBObject> parse(String[] fields) {
        //the doc
        BasicDBObject d = new BasicDBObject();

        //user_id
        d.put("user_id", fields[0]);
        //friend_id
        d.put("friend_id", fields[1]);

        //result
        return new Tuple<>(d, d);
    }
}
