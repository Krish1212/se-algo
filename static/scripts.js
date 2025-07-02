$(document).ready(function () {
    console.log('document loaded...')

    $('input[name="indexRadio"]').on('change', function () {
        var selectedIndex = $(this).val();
        loadSelectedIndex(selectedIndex)
    });

    function loadSelectedIndex(index = "NIFTY 100") {
        fetchUrl = '/index-data';
        if (index) {
            fetchUrl += `/${index}`
        }
        $.ajax({
            url: fetchUrl,
            success: async function (result) {
                $('#stocks-table').html(result)
            },
            failure: async function (error) {
                console.error("Failed to fetch data: ", error)
            },
            finally: function () { }
        })

    }

})