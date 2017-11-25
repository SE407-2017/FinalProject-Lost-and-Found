/**
 * Created by  on 2017/7/13.
 */

$(function () {
    //nav下划线条
    $('.nav li').click(
        function () {
            $('.nav li').removeClass('nav-active');
            $(this).addClass('nav-active');
        }
    );
    //左边栏效果
    $('.b-choose').click(
        function () {
            if($(this).children().not('span').css('display') == "none"||$(this).children().length<2) {
                $('.b-choose').children().not('span').css({'display': 'none'});
                $(this).children().not('span').css({'display': 'block'});
                $('.b-choose').css({'backgroundColor':'white','color':'#666'});
                $(this).css({'backgroundColor':'#3366FF','color':'white'});
            }else {
                $(this).children().not('span').css({'display': 'none'});
                $(this).css({'backgroundColor':'white','color':'#666'})
            }

        }
    );
    //鼠标移入变色
    $(".left-inner-bar li").mouseover(
        function () {
            $(this).css({'backgroundColor':'#e6e6e6'})
    }).mouseout(function () {
        $(this).css({'backgroundColor':'white'})
    });
    var arr = [],max = 100;
    for(var i = 1;arr.push(i++)<max;){}
    arr.sort(function () {
        return Math.random()-0.5;
    });

    $('.b-choose').click(function () {
        if($(this).children().length<2){
            $('.chart').css({'display':'none'});
            var name = $(this).attr('class').split('choose-')[1];
            $('.right-'+name).css({'display':'block'})
        }
    });
    $('.left-inner-bar li').click(function (event) {
        $('.chart').css({'display':'none'});
        var name1 = $(this).parents('.b-choose').attr('class').split('choose-')[1];
        var name2 = $(this).attr('class').split(name+'-')[1];
        $('.'+name1+'-'+name2).css({'display':'block'});
        event.stopPropagation();
    })
});