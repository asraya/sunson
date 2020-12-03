<template>

  <div id="all">

        <p><router-link :to="{ name: 'Create' }" class="btn btn-primary">Create</router-link>

        <div class="form-group">
            <input type="text" name="search" v-model="employeeSearch" placeholder="Search employee" class="form-control" v-on:keyup="searchEmployees">
        </div>

        <table class="table table-hover" style="width: 100%;">
            <thead>
            <tr>
                <td>ID</td>
                <td>Name Employee</td>
                <td>Division</td>
                <td>Thumbnail</td>
                <td>Date Updated</td>
                <td>Date Created</td>
                <td>Actions</td>
            </tr>
            </thead>

            <tbody>
                <tr v-for="employee in employees">
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.name_employee }}</td>
                    <td>{{ employee.division }}</td>
                    <td ><img :src="employee.thumbnail" width="50" height="50"/></td>
                    <td>{{ employee.date_updated }}</td>
                    <td>{{ employee.date_created }}</td>
                    <td>
                        <router-link :to="{name: 'EditEmployee', params: { id: employee.id }}" class="btn btn-primary fa fa-trash">Edit</router-link>
                        <router-link :to="{name: 'DeleteEmployee', params: { id: employee.id }}" class="btn btn-danger">Delete</router-link>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// import Punny from './Punny';

export default {
      data(){
          return{
              employees: [],
              originalEmployees: [],
              employeeSearch: ''
          }
      },
      created: function()
      {
          this.fetchEmployeeData();
      },
      methods: {
          fetchEmployeeData: function()
          {
              this.$http.get('http://localhost:5000/employee').then((response) => {
                  this.employees = response.body;
                  this.originalEmployees = this.employees;
                  for(var i = 0; i < this.employees.length; i++) {
                      this.employees[i].date_updated = new Date(this.employees[i].date_updated).toString();
                      this.employees[i].date_created = new Date(this.employees[i].date_created).toString();
                  }
              }, (response) => {
              });
          },
          searchEmployees: function()
          {
              if(this.employeeSearch == '')
              {
                  this.employees = this.originalEmployees;
                  return;
              }
              var searchedEmployees = [];
              for(var i = 0; i < this.originalEmployees.length; i++)
              {
                  var employeeTitle = this.originalEmployees[i]['name_employee'].toLowerCase();
                  if(employeeTitle.indexOf(this.employeeSearch.toLowerCase()) >= 0)
                  {
                      searchedEmployees.push(this.originalEmployees[i]);
                  }
              }
              this.employees = searchedEmployees;
          }
      }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  /*color: #00000;*/
}
#all {
    width: 1660px;
    margin: 0px 0px 0px 0px;
    background-color: #DCDCDC;
    margin-top: 100px;
    margin-bottom: 100px;
    margin-right: 0px;
    margin-left: 0px;
}

</style>
