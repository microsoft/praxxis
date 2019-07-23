# How to Contribute to praxxis

We'd love your help!

Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


## Installing praxxis 
run 
```
python setup.py develop
pip -r requirements-dev.txt 
``` 
to install the package in development mode and run m from the command line.

## Coding Standards
All changes made should follow [the PEP 8 style conventions](https://www.python.org/dev/peps/pep-0008/). Any new source files should have a header with descriptive information about what the file does. see the current files for an idea of the expected level of detail.

Overall, this project places a focus on useful, descriptive inline comments over block comments. The best changes will clearly document non-obvious sections of the code with inline or section comments. A single-line comment will suffice for most confusing sections or methods, at the programmer's discretion.

All code added should also pass the [tests](). Please run the pytest testset regularly as you work to ensure your code will not break any tests if it's pulled into the project.

As new functionality is added, please document the new features and add them to the tool's help page and the github readme.

## Making a Change
Before making a pull request, please open an issue! Discussing your proposed changes with the community will make your changes that much more valuable.
Once changes have been discussed, be sure that your code passes the tests before opening the pull request.
The smaller your changes are, the easier it is for them to be reviewed and merged.

Your pull request has the best chance of being merged if
- it includes tests for the new functionality
- it adds/alters a single functionality
- It includes tests for the new functionality
- Has a good commit message
  - subject line is 50 characters or less
  - uses imperative mood
  - body is wrapped at 72 characters
  - body is used to explain what and why

## Microsoft Open Source Code of Conduct

This code of conduct outlines expectations for participation in Microsoft-managed open source communities, as well as steps for reporting unacceptable behavior. We are committed to providing a welcoming and inspiring community for all. People violating this code of conduct may be banned from the community.

Our open source communities strive to:

* **Be friendly and patient:** Remember you might not be communicating in someone else's primary spoken or programming language, and others may not have your level of understanding.
* **Be welcoming:** Our communities welcome and support people of all backgrounds and identities. This includes, but is not limited to members of any race, ethnicity, culture, national origin, color, immigration status, social and economic class, educational level, sex, sexual orientation, gender identity and expression, age, size, family status, political belief, religion, and mental and physical ability.
* **Be respectful:** We are a world-wide community of professionals, and we conduct ourselves professionally. Disagreement is no excuse for poor behavior and poor manners. Disrespectful and unacceptable behavior includes, but is not limited to:
    * Violent threats or language.
    * Discriminatory or derogatory jokes and language.
    * Posting sexually explicit or violent material.
    * Posting, or threatening to post, people's personally identifying information ("doxing").
    * Insults, especially those using discriminatory terms or slurs.
    * Behavior that could be perceived as sexual attention.
    * Advocating for or encouraging any of the above behaviors.
* **Understand disagreements:** Disagreements, both social and technical, are useful learning opportunities. Seek to understand the other viewpoints and resolve differences constructively.
* This code is not exhaustive or complete. It serves to capture our common understanding of a productive, collaborative environment. We expect the code to be followed in spirit as much as in the letter.

## Scope
This code of conduct applies to all repos and communities for Microsoft-managed open source projects regardless of whether or not the repo explicitly calls out its use of this code. The code also applies in public spaces when an individual is representing a project or its community. Examples include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

Note: Some Microsoft-managed communities have codes of conduct that pre-date this document and issue resolution process. While communities are not required to change their code, they are expected to use the resolution process outlined here.  The review team will coordinate with the communities involved to address your concerns.

## Reporting Code of Conduct Issues
We encourage all communities to resolve issues on their own whenever possible. This builds a broader and deeper understanding and ultimately a healthier interaction. In the event that an issue cannot be resolved locally, please feel free to report your concerns by contacting [opencode@microsoft.com](mailto:opencode@microsoft.com).  Your report will be handled in accordance with the issue resolution process described in the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/).

In your report please include:

* Your contact information.
* Names (real, usernames or pseudonyms) of any individuals involved. If there are additional witnesses, please include them as well.
* Your account of what occurred, and if you believe the incident is ongoing. If there is a publicly available record (e.g. a mailing list archive or a public chat log), please include a link or attachment.
* Any additional information that may be helpful.

All reports will be reviewed by a multi-person team and will result in a response that is deemed necessary and appropriate to the circumstances. Where additional perspectives are needed, the team may seek insight from others with relevant expertise or experience. The confidentiality of the person reporting the incident will be kept at all times. Involved parties are never part of the review team.

Anyone asked to stop unacceptable behavior is expected to comply immediately. If an individual engages in unacceptable behavior, the review team may take any action they deem appropriate, including a permanent ban from the community.

_This code of conduct is based on the template established by the [TODO Group](http://todogroup.org/) and used by numerous other large communities (e.g., [Facebook](https://code.facebook.com/pages/876921332402685/open-source-code-of-conduct), [Yahoo](https://yahoo.github.io/codeofconduct), [Twitter](https://engineering.twitter.com/opensource/code-of-conduct), [GitHub](http://todogroup.org/opencodeofconduct/#opensource@github.com)) and the Scope section from the [Contributor Covenant version 1.4](http://contributor-covenant.org/version/1/4/)._
