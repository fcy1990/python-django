
$(function (){
    $('#submit-class').click(function(){

        var name = $('#class_name').val();
        var cid = $('#cid').val();
        console.log(name,cid);

        $.ajax({
            url:'clas_add',
            type:'post',
            data:{'class_name':name,'cid':cid},
            dataType:'JSON',
            success:function(data){
                console.log(data)
                if (data['status']){
                    location.href = '/class'
                }
                else {
                    alert('失败了，请重试！')
                }

            }
        })
         })
});
