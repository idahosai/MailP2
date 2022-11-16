document.addEventListener('DOMContentLoaded', function () {
    var modal = document.querySelector('.modal');
    M.Modal.init(modal);
})

// let tablebody = document.querySelector('.tablebody-data');
// let updatebtn = document.querySelector('.update-btn');

// updatebtn.addEventListener('on-click', function(){

//     let tr = document.createElement('<tr></tr>');

//     let titletd = document.createElement('<td name="title"><input></td>')
//     <td name="start_date">{{appointment.start_date}}</td>
//     <td name="end_date">{{appointment.end_date}}</td>
//     <td name="description">{{appointment.description}}</td>
//     <td>
//         <form id="edit-appointment" action="{% url 'edit-app' appointment.id %}"
//             method="POST">
//             {% csrf_token %}
//             <button class="update-btn btn btn-danger" type="submit">Update</button>
//         </form>
//     </td>
// })