// $("#openModal").onclick(function () {
//     console.log("musa")
// })

// $(document).ready(function () {
//     $(document).ready(function () {

//         $("#img_up_continue").click(function () {
//             let data = new FormData($("#ajax").get(0))
//             $.ajax({
//                 url: "{% url 'save_image' %}",
//                 method: "POST",
//                 data: data,
//                 processData: false,
//                 contentType: false,
//                 success: function (data) {
//                     $("#prev_image").attr('src', data['last_img_url'])
//                     $("#prev_title").text(data['title'])
//                     $("#div_span").text(data['title'])
//                 }
//             })
//         })
//     })

//     $(document).ready(function () {
        
//         $("#id_category").change(function () {
//             $(this).prop("checked")
//         })
//         $("#img_atwork_continue").click(function () {
//             console.log("Clicked atwork")
//             let description = $("#id_description").val()
//             let category = $("#id_category").val()
//             console.log(description, category)

//             let data = {
//                 'csrfmiddlewaretoken': '{{ csrf_token }}',
//                 category: category,
//                 description: description
//             }
//             $.ajax({
//                 url: "{% url 'atwork' %}",
//                 method: "POST",
//                 data: data,
//                 success: function (data) {
//                     console.log(data)
//                 }
//             })

//         })
//     })
//     $(document).ready(function () {

//         $("#publish_artwork").click(function () {
//             console.log("Clicked finish")
//             let is_uploaded = $("#is_uploaded").is(":checked");
//             console.log("is uploaded=", is_uploaded)

//             let data = {
//                 'csrfmiddlewaretoken': '{{ csrf_token }}',
//                 is_uploaded: is_uploaded
//             }
//             $.ajax({
//                 url: "{% url 'published_art_work' %}",
//                 method: "POST",
//                 data: data,
//                 dataType: "html",
//                 success: function (data) {
//                     console.log(data)
//                     $("#content_val").html(data);
//                 }
//             })

//         })
//     })

// }
// )