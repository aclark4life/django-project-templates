// UserMenu.js
import 'react';
import PropTypes from 'prop-types';

function handleLogout() {  // eslint-disable-line no-unused-vars
    window.location.href = '/accounts/logout';
}

const UserMenu = ({ isAuthenticated, isSuperuser }) => {
  return (
    <div>
      {isAuthenticated ? (
        <li className="nav-item dropdown">
          <a className="nav-link dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false"></a>
          <ul className="dropdown-menu">
            <li><a className="dropdown-item" href="/user/profile/">Profile</a></li>
            <li><a className="dropdown-item" href="/model-form-demo/">Model Form Demo</a></li>
            <li><a className="dropdown-item" href="/logging-demo/">Logging Demo</a></li>
            <li><a className="dropdown-item" href="/payments/">Payments Demo</a></li>
            {isSuperuser ? (
              <>
                <li><hr className="dropdown-divider"></hr></li>
                <li><a className="dropdown-item" href="/django" target="_blank">Django admin</a></li>
                <li><a className="dropdown-item" href="/api" target="_blank">Django API</a></li>
                <li><a className="dropdown-item" href="/wagtail" target="_blank">Wagtail admin</a></li>
                <li><a className="dropdown-item" href="/explorer" target="_blank">SQL Explorer</a></li>
              </>
            ) : null}
            <li><hr className="dropdown-divider"></hr></li>   
            <li><a className="dropdown-item" href="/accounts/logout">Logout</a></li>
          </ul>
        </li>
      ) : (
        <li className="nav-item">
          <a className="nav-link dropdown-toggle" type="button" aria-expanded="false" href="/accounts/login/"></a>
        </li>
      )}
    </div>
  );
};

UserMenu.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
  isSuperuser: PropTypes.bool.isRequired,
};

export default UserMenu;
