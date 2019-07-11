import React, {Component} from 'react';
import PropTypes from 'prop-types';

/**
 * This component is based on the Import sub-component of dash-grasia
 * See original implementation here:
 * https://github.com/Grasia/grasia-dash-components/blob/master/src/components/Import.react.js
 */

export default class Import extends Component {

  componentDidMount () {

    if (this.props.src) {
      //If source is given
      //We create a script whose src= points to that path but
      //specify that its loading should be deferred before
      //adding it to the document's body
      const {src} = this.props;
      const script = document.createElement('script');

      script.src = src;
      script.defer = true;

      document.body.appendChild(script);
      }
    }

  // This component does not render anything :)
  render() {
    return (null);
  }
}

Import.defaultProps = {};

Import.propTypes = {
  /**
  * The ID used to identify this component in Dash callbacks
  */
  id: PropTypes.string,

  /**
  * local or external source of the javascript to import
  */
  src: PropTypes.string

};

