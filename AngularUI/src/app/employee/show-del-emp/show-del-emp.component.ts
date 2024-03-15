import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-del-emp',
  templateUrl: './show-del-emp.component.html',
  styleUrls: ['./show-del-emp.component.css']
})
export class ShowDelEmpComponent  implements OnInit {

  constructor(private service:SharedService) { }

  EmployeeList: any=[];
  PhotoFilePath = this.service.PhotoUrl;

  EmployeeIdFilter:string="";
  EmployeeNameFilter:string="";
  DepartmentFilter:string="";
  EmployeeListWithoutFilter:any=[]

  ModalTitle:any;
  ActivateAddEditEmpComp:boolean=false;
  emp:any;

  ngOnInit(): void {
    this.refreshEmpList();
  }

  addClick() {
    this.emp = {
      EmployeeId:0,
      EmployeeName:"",
      Department:"",
      DateOfJoining:"",
      PhotoFileName:"dummy_dp.jpeg"
    }
    this.ModalTitle="Add Employee";
    this.ActivateAddEditEmpComp=true;
  }

  editClick(item:any) {
    this.emp=item;
    this.ModalTitle="Edit Employee";
    this.ActivateAddEditEmpComp=true;
  }

  closeClick(){
    this.ActivateAddEditEmpComp=false;
    this.refreshEmpList();
  }

  deleteClick(data:any){
    if(confirm('Are you sure??')){
      this.service.deleteEmployee(data.EmployeeId).subscribe(data=>{
        alert(data.toString());
        this.refreshEmpList();
      })
    }
  } 

  refreshEmpList(){
    this.service.getEmpList().subscribe((data) => {
      this.EmployeeList = data;
      this.EmployeeListWithoutFilter=data;
      console.log('JSON response = ',JSON.stringify(data));
      console.log(this.PhotoFilePath);
    });
  }
  
  FilterFn() {
    var EmployeeIdFilter = this.EmployeeIdFilter;
    var EmployeeNameFilter = this.EmployeeNameFilter;
    var DepartmentFilter = this.DepartmentFilter;

    this.EmployeeList = this.EmployeeListWithoutFilter.filter(function (event:any){
      return event.EmployeeId.toString().toLowerCase().includes(
        EmployeeIdFilter.toString().trim().toLowerCase()
      )&&
      event.EmployeeName.toString().toLowerCase().includes(
        EmployeeNameFilter.toString().trim().toLowerCase()
      )&&
      event.Department.toString().toLowerCase().includes(
        DepartmentFilter.toString().trim().toLowerCase()
      )
    });
  } 

  sortResult(prop:any,asc:any) {
    this.EmployeeList = this.EmployeeListWithoutFilter.sort(function(a:any,b:any){
      if(asc){
        return (a[prop]>b[prop])?1 : ((a[prop]<b[prop]) ?-1 :0);
      }
      else{
        return (b[prop]>a[prop])?1 : ((b[prop]<a[prop]) ?-1 :0);
      }
    })
  }
}

