CPU virtualization

- user의 실제 cpu는 제한되어 있지만, os의 어떤 동작으로 인해 user에게 무한개의 cpu가 있는 것과 같은 illusion을 제공한다.
- => "time-sharing"을 통해!

<br>

두 가지 time-sharing 정책

1. context switch
   - time slice가 다 되어서 timer가 interrupt를 주면 해당 프로그램은 멈춘다.
   - 그러나, 해당 프로그램은 언젠가 다시 수행될 수 있다.
   - 사용자는 단 한번도 끊이지 않은 것처럼 illusion을 제공받아야 한다.
   - => 한번도 멈추지 않은 것처럼 멈췄을 때의 상태에 대한 모든 정보를 저장하고, 다시 시작할 때 re-set 해줘야 한다!
   - => register의 값을 context라 한다. 해당 context를 계속해서 switch 해줄 수 있어야 한다!
2. scheduling policies
   - 어떤 프로그램을 "먼저" 수행할 지도 결정할 수 있어야 한다!

<br>

Process

- 현재 수행(running) 중인 프로그램의 묶음
- program은 파일이란 형태로 디스크에 저장됨. 해당 program이 메모리에 올라와서 실행될 수 있는 형태로 바뀌어져 cpu가 접근해서 수행할 수 있는 것이 process.
- => 다양한 상태(state)를 가짐. 기다리는 상태.... 등

<br>

Process API (Application Program Interface)

- 사용자가 쉽게 이용할 수 있는 인터페이스를 제공하지만, 실제 수행은 OS에서
- ex) process creation: disk에 있는 프로그램을 메모리로 가져온다.

<br>

Process States - (3-State Model)

![IMG_AAE5027E018F-1](image.assets/IMG_AAE5027E018F-1.jpeg)

- Running
  - 수행에 필요한 모든 resource를 가짐 + cpu에 대한 권한을 가짐
- Ready
  - 수행에 필요한 모든 resource를 가짐. 그러나 cpu에 대한 권한은 가지지 못함
  - scheduling policy에 따라 cpu에 대한 권한만 주면, 얼마든지 running 상태로 변할 수 있음
- Blocked(Wait)
  - 수행에 필요한 모든 resource를 가지지 못함 + cpu에 대한 권한도 가지지 못함
  - I/O를 요청한 상태 (외부 I/O 장치에, 수행에 필요한 resource를 요청) ex) scanf .. page fault ..
  - I/O에 대한 요청이 와서(I/O가 done해서) 모든 resource를 가지더라도, cpu에 대한 권한은 아직 없으므로, ready 상태로 가서 os가 권한을 줄 때까지 기다림
- 이때, descheduled는 timer interrupt라 보면 된다. scheduled는 scheduling policy에 의해 권한을 받은 것이라 보면 된다.