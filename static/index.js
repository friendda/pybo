
$(document).ready(function(){
    $(".page-link").on('click', function() {
        $("#page").val($(this).data("page"));
        $("#searchForm").submit();
    });
//기본검색
    $("#btn_search").on('click', function() {
        $("#kw").val($(".kw").val());
		$("#page").val(1);  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
        $("#searchForm").submit();
    });
//다중검색
	$("#btn_m_search").on('click', function() {
        $("#mkw1").val($(".mkw1").val());
		$("#mkw2").val($(".mkw2").val());
		$("#mkw3").val($(".mkw3").val());
		$("#mkw4").val($(".mkw4").val());
		$("#mkw5").val($(".mkw5").val());
		$("#mkc1").val($(".mkc1").val());
		$("#mkc2").val($(".mkc2").val());
		$("#mkc3").val($(".mkc3").val());
		$("#mkc4").val($(".mkc4").val());
		$("#mkc5").val($(".mkc5").val());
		$("#page").val(1);  // 검색버튼을 클릭할 경우 1페이지부터 조회한다.
        $("#searchForm").submit();
	  });
});


//로딩바
$(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);

//전체삭제 확인
function button_event(){
if (confirm("모든 데이터가 삭제됩니다. 정말 삭제하시겠습니까??") == true){    //확인

    $("#deleteForm").submit();
}else{   //취소
    return;
}
}


//선택 order 전송

function order_submit(frm){
	if(confirm("발주요청 하시겠습니까?") == true){
		frm.action=orderpage;
		frm.submit();
	}else{
	return ;
	}
}



//선택 삭제
  function submit2(frm) { 
    frm.action=delpage; 
    frm.submit(); 
	return true; 
  } 

  //order_선택 삭제
  function submit3(frm) { 
    frm.action=orddelpage; 
    frm.submit(); 
	return true; 
  } 

//검색된 전체 다운로드
   $("#btn_down").on('click', function() {
        $("#downform").submit();
    });

//체크박스 전체선택
  function selectAll(selectAll)  {
  const checkboxes 
     = document.querySelectorAll('input[type="checkbox"]');
  
  checkboxes.forEach((checkbox) => {
    checkbox.checked = selectAll.checked
  })
}

//다중검색 toggle
$(function (){
    $("#t_button").click(function (){
    $("#divToggle").toggle();
	
	  
	  if($("#divToggle").is(":hidden")){
		  $("#basic").show(); }
		else {$("#basic").hide();}
   }); 
 });

//upload -modal button
$("#menu-excel").click(function () {
        $("#modal-excel").modal('show');
    });


//excel_upload    (forced reflow while executing javascript)

function excel_upload(){
            if(!$('#file_excel').val()){
                alert('엑셀 파일을 입력하세요');
            }else{

                var ext = $('#file_excel').val().split('.').pop().toLowerCase();
                if($.inArray(ext, ['xls','xlsx']) == -1) {
	                alert('엑셀 파일만 업로드 할 수 있습니다.');
                }else{
                    if (confirm('엑셀을 반영 하시겠습니까?')){

                       var ajax_url = uppage;

                       // Get form
                       var form = $('#frm_excel')[0];

                       // Create an FormData object
                       var formData = new FormData(form);

                       var params = "";
                       var msg = "";
                       $.ajax({
                           type: "post",
                           enctype: 'multipart/form-data',
                           processData: false,
                           contentType: false,
						   url: ajax_url,
                           //data:params,
                           data: formData,
                           dataType: "JSON", // JSON 리턴
                           headers:{"X-CSRFTOKEN": '{{csrftoken}}'},
                           beforeSend: function () {
                           },
                           success: function (data) {
                               // success
                               alert(data.rtnmsg);
                               if (data.status) {
                                   location.reload();
                               }
                           },
                           complete: function (data) {
                               // 통신이 실패했어도 완료가 되었을 때
                           },
                           error: function(xhr,status,error){

										alert("통신 에러");
									
                           },
                           timeout: 500000 //응답제한시간 ms
                       });

                    }
                }
            }
        }

//공지_팝업창

$('.btn-example').click(function(){
        var $href = $(this).attr('href');
        layer_popup($href);
    });
    function layer_popup(el){

        var $el = $(el);//레이어의 id를 $el 변수에 저장
        var isDim = $el.prev().hasClass('dimBg');//dimmed 레이어를 감지하기 위한 boolean 변수

        isDim ? $('.dim-layer').fadeIn() : $el.fadeIn();

        var $elWidth = ~~($el.outerWidth()),
            $elHeight = ~~($el.outerHeight()),
            docWidth = $(document).width(),
            docHeight = $(document).height();

        // 화면의 중앙에 레이어를 띄운다.
        if ($elHeight < docHeight || $elWidth < docWidth) {
            $el.css({
                marginTop: -$elHeight /2,
                marginLeft: -$elWidth/2
            })
        } else {
            $el.css({top: 0, left: 0});
        }

        $el.find('a.btn-layerClose').click(function(){
            isDim ? $('.dim-layer').fadeOut() : $el.fadeOut(); // 닫기 버튼을 클릭하면 레이어가 닫힌다.
            return false;
        });

        $('.layer .dimBg').click(function(){
            $('.dim-layer').fadeOut();
            return false;
        });

    }