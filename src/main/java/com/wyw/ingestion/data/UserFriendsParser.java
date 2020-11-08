package com.wyw.ingestion.data;

import com.wyw.ingestion.common.Parsable;

public abstract class UserFriendsParser<T> implements Parsable<T> {
    //check if the record is a header
    @Override
	public Boolean isHeader(String[] fields) {
        //check
        return (isValid(fields) && fields[0].equals("user_id") && fields[1].equals("friend_id"));
    }

    //check if a record is valid
    @Override
    public Boolean isValid(String[] fields) {
        //check
        return (fields.length > 1 && !isEmpty(fields, new int[] { 0, 1 }));
    }
}
