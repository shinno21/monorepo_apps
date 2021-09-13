import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-any-page',
  templateUrl: './any-page.component.html',
  styleUrls: ['./any-page.component.scss']
})
export class AnyPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    console.log("Hello Angular")
  }

}
