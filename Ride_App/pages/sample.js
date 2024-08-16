
import React from 'react'

const sample = () => {
  return (
    <div>
        {/* <!-- =============== Navigation ================ --> */}
        <div class="container">
          <div class="navigation">
            <ul>
              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="logo-apple"></ion-icon>
                  </span>
                  <span class="title">Brand Name</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="home-outline"></ion-icon>
                  </span>
                  <span class="title">Dashboard</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="people-outline"></ion-icon>
                  </span>
                  <span class="title">Customers</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="chatbubble-outline"></ion-icon>
                  </span>
                  <span class="title">Messages</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="help-outline"></ion-icon>
                  </span>
                  <span class="title">Help</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="settings-outline"></ion-icon>
                  </span>
                  <span class="title">Settings</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="lock-closed-outline"></ion-icon>
                  </span>
                  <span class="title">Password</span>
                </a>
              </li>

              <li>
                <a href="#">
                  <span class="icon">
                    <ion-icon name="log-out-outline"></ion-icon>
                  </span>
                  <span class="title">Sign Out</span>
                </a>
              </li>
            </ul>
          </div>

          {/* <!-- ========================= Main ==================== --> */}
          <div class="main">
            <div class="topbar">
              <div class="toggle">
                <ion-icon name="menu-outline"></ion-icon>
              </div>

              <div class="search">
                <label>
                  <input type="text" placeholder="Search here" />
                  <ion-icon name="search-outline"></ion-icon>
                </label>
              </div>

              <div class="user">
                <img src="assets/imgs/customer01.jpg" alt="" />
              </div>
            </div>
            {/* 
            <!-- ======================= Cards ================== --> */}
            <div class="cardBox">
              <div class="card">
                <div>
                  <div class="numbers">1,504</div>
                  <div class="cardName">Daily Views</div>
                </div>

                <div class="iconBx">
                  <ion-icon name="eye-outline"></ion-icon>
                </div>
              </div>

              <div class="card">
                <div>
                  <div class="numbers">80</div>
                  <div class="cardName">Sales</div>
                </div>

                <div class="iconBx">
                  <ion-icon name="cart-outline"></ion-icon>
                </div>
              </div>

              <div class="card">
                <div>
                  <div class="numbers">284</div>
                  <div class="cardName">Comments</div>
                </div>

                <div class="iconBx">
                  <ion-icon name="chatbubbles-outline"></ion-icon>
                </div>
              </div>

              <div class="card">
                <div>
                  <div class="numbers">$7,842</div>
                  <div class="cardName">Earning</div>
                </div>

                <div class="iconBx">
                  <ion-icon name="cash-outline"></ion-icon>
                </div>
              </div>
            </div>

            {/* <!-- ================ Order Details List ================= --> */}
            <div class="details">
              <div class="recentOrders">
                <div class="cardHeader">
                  <h2>Recent Orders</h2>
                  <a href="#" class="btn">
                    View All
                  </a>
                </div>
              </div>

              {/* <!-- ================= New Customers ================ --> */}
              <div class="recentCustomers">
                <div class="cardHeader">
                  <h2>Recent Customers</h2>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  );
}

export default sample

