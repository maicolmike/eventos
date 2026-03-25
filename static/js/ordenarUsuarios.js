document.addEventListener("DOMContentLoaded", function() {
                setTimeout(function() {
                    $('#example1').DataTable().order([0, 'asc']).draw();
                }, 100);
            });