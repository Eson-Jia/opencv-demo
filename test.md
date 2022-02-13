```js
db.alarm.update({
    _id:1,
    $or: [
        {state: {$ne: 1}},
        {lastModifies:{$gt:10000}},
    ],
}, {
    $set:{
        state:1,
        lastModifies:10000,
    },
})
```