function troca() {
    document.getElementById("login").style.display="none";
    document.getElementById("reset").style.display="block";
    }

    $( document ).ready(function() {
        var dimg = "../static/images/coracaoAntes.png";
        var imgswitch = false;
        $('.btnCurtir').click(function(){
            if(imgswitch){
                 $(this).attr('src','../static/images/coracaoAntes.png');
                 imgswitch = false;
            }else{
                 $(this).attr('src','../static/images/coracaoDepois.png');
                 imgswitch = true;
                 curtir += 1;
            }
        })
    });

    var loadFile = function(event) {
        var output = document.getElementById('output');
        output.src = URL.createObjectURL(event.target.files[0]);
        output.onload = function() {
          URL.revokeObjectURL(output.src) // free memory
        }
      };