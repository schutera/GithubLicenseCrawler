# GithubLicenseCrawler

This script is intended to crawl license information of repositories through the GitHub API.
Taking a csv file with requirements.txt format the script will return a csv with the associated license information.

# Input
Input file is expected to be a requirements.txt
Expected format looks like this, for two exemplary repositories:

```
HeartSeg-Dataset==0.0.1
DeepDive==0.0.1
```

# Output
Output file will be generated on the fly, named licenses.csv and the columns depict:

| Repo name | Repo Url | License name | License Url |

![image](https://user-images.githubusercontent.com/42141561/194750006-4e34cf51-777f-4f03-8058-d8883060e6c8.png)

# Running the script should look like this:
![image](https://user-images.githubusercontent.com/42141561/147765292-a802ddf3-a872-4026-8eea-3053c882fd1e.png)


# Contact and Contribute 
mark.schutera@gmail.com
Obviously the Github API is way more powerful than what has been done here. Feel free to extend this code or preferably directly contribute here.

Future work can include..

.. a function to input for what purpose you want to use your own project, which then highlights packages with conflicting licenses.

.. a function that recurrently walks through the licenses of the packages you included, and the ones they included, and the ones they included, and so on.

