# -*-coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app01.db import DBConnect
import json
from app01.log import Logger

logger = Logger(logger="add_class").getlog()

def query_class(request):
    if request.method == 'GET':
        db=DBConnect()
        sql = 'select cid, cname from class'
        result = db.Fetchall(sql)
        print(result)
        return render(request,'query_class.html',{'result':result})

def add_class(request):
    db = DBConnect()
    if request.method == 'GET':
        sql = 'select max(cid) from class'
        cid = db.Fetchone(sql)
        logger.info(cid)
        cid = int(cid['max(cid)']) + 1
        logger.info('cid'+str(cid))
        return render(request,'add_class.html',{'cid':cid})
    else:
        ret = {'status': None, 'message': None}
        try:
            name = request.POST.get('class_name')
            logger.info('+++' + str(name))
            cid = request.POST.get('cid')
            logger.info('+++' + str(cid))
            db.Add("insert into class(cid,cname) values('%s','%s');" % (cid,name))
            cname=db.Fetchone("select cname from class where cid=%s " % cid)
            logger.info('@@@@@' + str(cname))
            ret['status'] = True
            ret['message']='添加成功'
        except Exception as e:
            ret['status'] = False
            ret['message'] = e
        return HttpResponse(json.dumps(ret))


def edit_class(request):
    pass

def del_class(request):
    db = DBConnect()
    cid = request.GET.get(id)
    logger.info(cid)
    sql = 'delete from class where cid = %s, % (cid)'
    db.Del(sql)
    return redirect('/class')


if __name__ == '__main__':
   pass