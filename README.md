# TapArt-Artists-Subdomain

<!--
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/
  
  /repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TapArt Subdomain</h3>

  <p align="center">
    A webapp for artists to share their art with the world!
    <br />
    <a href="https://github.com/musakhan17/TapArt-Artists-Subdomain"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/musakhan17/TapArt-Artists-Subdomain/issues">Report Bug</a>
    ·
    <a href="https://github.com/musakhan17/TapArt-Artists-Subdomain/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

```sh
.
├── accounts                    <-- Accounts Page
├── pages                       <-- Designs Page
├── static                      <-- static files (bootsrap, jquery etc.)
├── tapart                      <-- Project files
├── templates                   <-- Project Templates
├── README.md                   <-- This instructions file
├── manage.py                   <-- Deployment script
└── requirements.txt            <-- SAM template
```

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`


### Built With

* [Django](https://djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [AWS Services]()


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
```sh
npm install npm@latest -g
```

### Installation

1. Clone the repo
```sh
gh repo clone musakhan17/TapArt-Artists-Subdomain
```
2. Install Python and required packages
```
$ brew install python
```

3. Create your own virtual environment
```sh
$ python3 -m venv tapart
$ source venv/bin/activate
```

4. Install your requirements
```sh
pip install -r requirements.txt
```

5. Create a new PostgreSQL database
```sh
$ psql postgres
$ CREATE DATABASE databasename
$ \connect databasename
```

6. Generate a new secret key
Visit [Djecrety](https://djecrety.ir/) to quickly generate a secure secret key
Use the command below to create a .env file to secure my secret key and database credentials.
```sh
$ psql postgres
$ CREATE DATABASE databasename
$ \connect databasename
```

7. Make your migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

8. Create a new superuser
```sh
$ python manage.py createsuperuser
```

9. Final checks
Start the development server and ensure everything is running without errors.
```sh
$ python manage.py runserver
```

10. Important!
Please, make any changes in a separate branch. Do not, make any changes, in the master branch. Good luck!

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/musakhan17/TapArt-Artists-Subdomain/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Musa Khan - [@ChiknaMoulvi](https://twitter.com/ChiknaMoulvi) - musakhan.10@gmail.com
Khawaja Abdul Ahad - [@kaa125](https://twitter.com/kaa125) - kaa125@gmail.com

Project Link: [https://github.com/musakhan17/TapArt-Artists-Subdomain](https://github.com/musakhan17/TapArt-Artists-Subdomain)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=flat-square
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: images/screenshot.png
