window.onload = function(){
    var eid = ['#id_content','#id_body', '#id_description', '#id_summary', '#id_quote', '#id_banner_text'];
    for(i=0;i<eid.length;i++){
        if(django.jQuery(eid[i]).length){
            django.jQuery('label[for=' + eid[i] + ']').css({
                display:"block",
                clear:"both",
                width:"100%",
                height:"18px"
            });

            django.jQuery('<div id="contentElement" style="display:block; clear:both; width:100%;height:3px"></div>').insertBefore(eid[i]);
        }
    }
}

window.popup_window_input = "";

function CustomFileBrowser (field_name, url, type, win) {
    window.popup_window_input = field_name;
    tinyMCE.activeEditor.windowManager.open({
        url : "/admin/filebrowser/browse/?pop=2",
        title : 'My File Browser',
        close_previous : "no",
        width : 920, height : 550
    }, {
        window : win,
        input : field_name,
        custom_param : 1,
        resizable : "no",
        inline: "no"
    });
    return false;
}

tinyMCE.init({
    mode : "textareas",
    plugins : 'advlist link image charmap print preview textcolor table fullscreen code',
    height: 300,
    toolbar: "save | undo redo | styleselect | bold italic underline | outdent indent | numlist bullist | alignleft aligncenter alignright alignjustify |  forecolor backcolor table  | charmap link image | fullscreen code",
    width: "100%",
    image_advtab: true,
    file_browser_callback : CustomFileBrowser,
    convert_urls : false
});

window.active_editor = tinyMCE;
