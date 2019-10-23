from django.shortcuts import render,HttpResponse,redirect
import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def query(request):
    if request.method == 'GET':
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        sql = 'select id, name from claes'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        cursor.close()
        con.close()
        return render(request, 'query.html',{'result': result})

def add(request):
    if request.method == 'GET':
        return render(request,'add.html')
    else:
        name = request.POST.get('name')
        if name == '':
            return render(request,'add.html',{'errormessage': '班级名称不能为空'})
        else:
            con = sqlite3.connect('fcy.db')
            con.row_factory = dict_factory
            cursor = con.cursor()
            cursor.execute('select id from claes order by id desc limit 1')
            res = cursor.fetchone()
            id = res['id']
            id = int(id) +1
            cursor.execute('insert into claes(id,name) values (?,?)',[id,name,])
            con.commit()
            cursor.close()
            con.close()
            return redirect('/query')

def delete(request):
    id = request.GET.get('id')
    con = sqlite3.connect('fcy.db')
    con.row_factory = dict_factory
    cursor = con.cursor()
    cursor.execute('delete from claes where id=?', [id, ])
    con.commit()
    cursor.close()
    con.close()
    return redirect('/query')

def edit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select id,name from claes where id=?',[id,])
        result = cursor.fetchone()
        print(result)
        cursor.close()
        con.close()
        return render(request,'edit.html',{'result':result})
    else:
        id = request.GET.get('nid')
        name = request.POST.get('name')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('update claes set name=? where id=?',[name,id,])
        con.commit()
        cursor.close()
        con.close()
        return redirect('/query')

def query_student(request):
    if request.method == 'GET':
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select student.id, student.s_name, student.cid,c.classID from student left join claes c on student.cid = c.name')
        result = cursor.fetchall()
        print(result)
        cursor.execute('select id, name,classID from claes')
        res = cursor.fetchall()
        print(res)
        cursor.close()
        con.close()
        return render(request,'query_student.html',{'result':result,'res':res})

def add_student(request):
    if request.method == 'GET':
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select id, name,classID from claes')
        result = cursor.fetchall()
        print(result)
        cursor.close()
        con.close()
        return render(request, 'add_student.html', {'result': result})
    else:
        name = request.POST.get('name')
        classid = request.POST.get('cid')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select id from student order by id desc limit 1')
        res = cursor.fetchone()
        id = res['id']
        id = int(id) + 1
        cursor.execute('select name from claes where classID=?', [classid, ])
        cid = cursor.fetchone()
        print(cid['name'])
        cursor.execute('insert into student(id,s_name,cid) values (?,?,?)', [id, name, cid['name'],])
        con.commit()
        cursor.close()
        con.close()
        return redirect('/student')

def modal_add_student(request):
    ret = {'status':True, 'message':None}
    try:
        sname = request.POST.get('sname')
        cname = request.POST.get('cname')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select id from student order by id desc limit 1')
        res = cursor.fetchone()
        print(res)
        id = res['id']
        print(id)
        nid = int(id) + 1
        print(nid)
        cursor.execute('insert into student(id,s_name,cid) values (?,?,?)', [nid, sname, cname,])
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def modal_edit_student(request):
    ret = {'status':True,'message':True}
    try:
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        classId = request.POST.get('classId')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute(
            'update student set s_name=? , cid = (select name from claes where classID = ?) where id=?',[sname,classId,sid])
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))

def modal_del_student(request):
    ret = {'status':True,'message':True}
    try:
        studentId = request.POST.get('studentId')
        # studentName = request.POST.get('studentName')
        # classID = request.POST.get('classID')
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute(
            'delete from student where id=?',[studentId,])
        con.commit()
        cursor.close()
        con.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))

#多对多
def query_teachers(request):
    if request.method == 'GET':
        con = sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select tid, tname,tclass from teachers')
        result = cursor.fetchall()
        print(result)
        cursor.close()
        con.close()
        return render(request, 'query_teachers.html', {'result': result})


def edit_teachers(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(id)
        con=sqlite3.connect('fcy.db')
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute('select tid, tname,tclass from teachers where tid=?',[id,])
        result=cursor.fetchone()
        print(result)
        # cursor.execute('select ')
        cursor.close()
        con.close()
        return render(request,'edit_teachers.html',{'result':result})
    else:
        pass

def del_teachers(request):
    pass