# Getting Started with Our Interface

To ensure a seamless experience with our interface, please follow the instructions below to set up the environment and explore the functionalities designed for accessing our corpus and annotations data.

## Environment Setup

Begin by setting up the Docker environment to run our application. Execute the following commands in your terminal:

1.  Build the Docker image:

    ```         
    docker build -t web_development .
    ```

2.  Start the application by running the Docker container:

    ```         
    docker run -p 8501:8501 web_development
    ```

3.  Once the container is running, you can access our Streamlit app through your web browser at the following URL:

    ```         
    http://localhost:8501
    ```

Please note, the application is hosted on port 8501.

## Exploring the Interface

Our interface offers multiple ways to access and explore the corpus and annotations data. We encourage peer reviewers to experiment with the following functionalities:

-   **Search by Name**: Enter the name of a university to access a comprehensive introduction. This feature retrieves the main corpus text associated with the specified university.

-   **Search by Filter**: Use this function to discover relevant university data. Selection can be made based on various filtering indicators, which correspond to annotated tags within our data set.

-   **Search for Similar Universities**: By inputting a university's name, this search will yield a list of universities sharing similar characteristics, as determined by their annotated tags.

Thank you for contributing to the refinement of our project. Your insights are invaluable to us.
