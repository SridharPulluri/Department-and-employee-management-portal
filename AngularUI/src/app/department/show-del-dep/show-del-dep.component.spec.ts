import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowDelDepComponent } from './show-del-dep.component';

describe('ShowDelDepComponent', () => {
  let component: ShowDelDepComponent;
  let fixture: ComponentFixture<ShowDelDepComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowDelDepComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowDelDepComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
